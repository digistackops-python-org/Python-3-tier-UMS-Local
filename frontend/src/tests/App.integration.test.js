import { render, screen, fireEvent } from '@testing-library/react';
import App from '../App';

describe('App Integration Test', () => {

  test('navigates from home to add employee page', () => {
    render(<App />);

    fireEvent.click(screen.getByText(/Add Employee/i));
    expect(screen.getByText(/Add SapSecOps Employee/i)).toBeInTheDocument();
  });

  test('navigates from home to employee list', () => {
    render(<App />);

    fireEvent.click(screen.getByText(/Employee List/i));
    expect(screen.getByText(/SapSecOps Employee List/i)).toBeInTheDocument();
  });
});
