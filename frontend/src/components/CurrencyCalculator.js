import { useState } from 'react';
import React from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

function CurrencyCalculator() {
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs((values) => ({ ...values, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setInputs(() => '5');
    console.log(inputs);
  };

  /*return (
    <center>
      <form onSubmit={handleSubmit}>
        <label>
          Enter your name:
          <input
            type="text"
            name="username"
            value={inputs.username || ''}
            onChange={handleChange}
          />
        </label>
        <br></br>
        <label>
          Enter your age:
          <input
            type="number"
            name="age"
            value={inputs.age || ''}
            onChange={handleChange}
          />
        </label>
        <br></br>
        <input type="submit" />
      </form>
    </center>
  );*/
  return (
    <Form>
      <center>
        <Form.Group
          className="mb-3 w-25 mt-5"
          controlId="formBasicCurrencyFrom"
        >
          <Form.Label>Currency From</Form.Label>
          <Form.Select>
            <option>Please choose currency to give</option>
            <option value="1">American Dollar</option>
            <option value="2">Euro</option>
            <option value="3">Pound Sterling</option>
            <option value="4">Polish Zloty</option>
          </Form.Select>
          <br />
          <Form.Control type="Currency From" placeholder="Enter currency" />
          <br />
        </Form.Group>

        <Form.Group className="mb-3 w-25" controlId="formBasicCurrencyTo">
          <Form.Label>Currency To</Form.Label>
          <Form.Select>
            <option>Please choose currency to get</option>
            <option value="1">American Dollar</option>
            <option value="2">Euro</option>
            <option value="3">Pound Sterling</option>
            <option value="4">Polish Zloty</option>
          </Form.Select>
          <br />
          <Form.Control type="Currency To" placeholder="Get the result" />
        </Form.Group>
        <Button variant="primary" type="submit">
          Calculate
        </Button>
      </center>
    </Form>
  );
}

export default CurrencyCalculator;
