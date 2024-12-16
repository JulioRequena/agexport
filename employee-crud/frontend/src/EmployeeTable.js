import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EmployeeTable = () => {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/employees')  // URL del backend Flask
      .then(response => {
        setEmployees(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the employees!", error);
      });
  }, []);

  return (
    <div className="container">
      <h2>Employee List</h2>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Last Name</th>
            <th>Salary</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(employee => (
            <tr key={employee.id}>
              <td>{employee.id}</td>
              <td>{employee.name}</td>
              <td>{employee.last_name}</td>
              <td>{employee.salary}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeTable;
