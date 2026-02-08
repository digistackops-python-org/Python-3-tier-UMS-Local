import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import EmployeeList from '../EmployeeList';
import axios from 'axios';

jest.mock('axios');

const mockEmployees = [
  {
    _id: '1',
    name: 'John',
    email: 'john@test.com',
    designation: 'DevOps',
    salary: 120000
  }
];

describe('EmployeeList Component', () => {

  test('fetches and displays employees', async () => {
    axios.get.mockResolvedValueOnce({ data: mockEmployees });

    render(<EmployeeList onEdit={jest.fn()} />);

    expect(await screen.findByText('John')).toBeInTheDocument();
    expect(screen.getByText('DevOps')).toBeInTheDocument();
  });

  test('delete employee', async () => {
    axios.get.mockResolvedValueOnce({ data: mockEmployees });
    axios.delete.mockResolvedValueOnce({});

    window.confirm = jest.fn(() => true);

    render(<EmployeeList onEdit={jest.fn()} />);

    const deleteBtn = await screen.findByRole('button', { name: /Delete/i });
    fireEvent.click(deleteBtn);

    await waitFor(() => {
      expect(axios.delete).toHaveBeenCalled();
    });
  });

  test('edit button triggers callback', async () => {
    axios.get.mockResolvedValueOnce({ data: mockEmployees });
    const onEdit = jest.fn();

    render(<EmployeeList onEdit={onEdit} />);

    fireEvent.click(await screen.findByRole('button', { name: /Edit/i }));
    expect(onEdit).toHaveBeenCalledWith(mockEmployees[0]);
  });
});
