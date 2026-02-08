import { render, screen, fireEvent } from '@testing-library/react';
import AddEmployee from '../AddEmployee';
import axios from 'axios';

jest.mock('axios');

describe('AddEmployee Component', () => {

  test('renders add employee form', () => {
    render(<AddEmployee onFinished={jest.fn()} />);
    expect(screen.getByText(/Add SapSecOps Employee/i)).toBeInTheDocument();
  });

  test('submits new employee data', async () => {
    axios.post.mockResolvedValueOnce({ data: {} });

    const onFinished = jest.fn();
    render(<AddEmployee onFinished={onFinished} />);

    fireEvent.change(screen.getByPlaceholderText('Name'), {
      target: { value: 'John Doe' }
    });
    fireEvent.change(screen.getByPlaceholderText('Email'), {
      target: { value: 'john@example.com' }
    });
    fireEvent.change(screen.getByPlaceholderText('Designation'), {
      target: { value: 'DevOps Engineer' }
    });
    fireEvent.change(screen.getByPlaceholderText('Salary'), {
      target: { value: '100000' }
    });

    fireEvent.click(screen.getByRole('button', { name: /Add Employee/i }));

    expect(axios.post).toHaveBeenCalledTimes(1);
    expect(onFinished).toHaveBeenCalled();
  });

  test('updates employee when editing', async () => {
    axios.put.mockResolvedValueOnce({ data: {} });

    const employeeToEdit = {
      _id: '123',
      name: 'Jane',
      email: 'jane@test.com',
      designation: 'Manager',
      salary: 90000
    };

    render(
      <AddEmployee employeeToEdit={employeeToEdit} onFinished={jest.fn()} />
    );

    fireEvent.click(screen.getByRole('button', { name: /Update Employee/i }));

    expect(axios.put).toHaveBeenCalledWith(
      expect.stringContaining('/employees/123'),
      expect.any(Object)
    );
  });
});
