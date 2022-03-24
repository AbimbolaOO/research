import { useEffect } from "react";
import { Formik, Field, Form } from "formik";
import axios from "axios";

axios.defaults.withCredentials = true;

function App() {
  useEffect(() => {
    const connectToApi = async () => {
      try {
        const { data } = await axios("/ok");
        console.log("######", "api ok");
      } catch (err) {
        console.log(err);
      }
    };
    connectToApi();
  }, []);

  const onSubmit = async (values) => {
    try {
      const { data } = await axios({
        method: "post",
        url: "/create",
        data: {
          ...values,
        },
      });
      console.log("*****", data);
    } catch (err) {
      console.log(err);
    }
  };

  const onSubmit2 = async (values) => {
    try {
      const { data } = await axios({
        method: "post",
        url: "/create2",
        data: {
          ...values,
        },
      });
      console.log(">>>>", data);
    } catch (err) {
      console.log(err);
    }
  };

  const onSubmit3 = async (values) => {
    try {
      const { data } = await axios({
        method: "post",
        withCredentials: true,
        url: "/getCookie",
        data: {
          ...values,
        },
      });
      console.log("||||||", data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <h1>Form 1 for create1 </h1>
      <Formik
        initialValues={{
          firstName: "",
          lastName: "",
          email: "",
        }}
        onSubmit={onSubmit}
      >
        <Form>
          <label htmlFor="firstName">First Name</label>
          <Field id="firstName" name="firstName" placeholder="Jane" />

          <label htmlFor="lastName">Last Name</label>
          <Field id="lastName" name="lastName" placeholder="Doe" />

          <label htmlFor="email">Email</label>
          <Field
            id="email"
            name="email"
            placeholder="jane@acme.com"
            type="email"
          />
          <button type="submit">Submit</button>
        </Form>
      </Formik>

      <h1>Form 2 for create2 that returns null has response </h1>
      <Formik
        initialValues={{
          firstName: "",
          lastName: "",
          email: "",
        }}
        onSubmit={onSubmit2}
      >
        <Form>
          <label htmlFor="firstName">First Name</label>
          <Field id="firstName" name="firstName" placeholder="Jane" />

          <label htmlFor="lastName">Last Name</label>
          <Field id="lastName" name="lastName" placeholder="Doe" />

          <label htmlFor="email">Email</label>
          <Field
            id="email"
            name="email"
            placeholder="jane@acme.com"
            type="email"
          />
          <button type="submit">Submit</button>
        </Form>
      </Formik>

      <h1>Form 3 for getCookie that returns null has response </h1>
      <Formik
        initialValues={{
          firstName: "",
          lastName: "",
          email: "",
        }}
        onSubmit={onSubmit3}
      >
        <Form>
          <label htmlFor="firstName">First Name</label>
          <Field id="firstName" name="firstName" placeholder="Jane" />

          <label htmlFor="lastName">Last Name</label>
          <Field id="lastName" name="lastName" placeholder="Doe" />

          <label htmlFor="email">Email</label>
          <Field
            id="email"
            name="email"
            placeholder="jane@acme.com"
            type="email"
          />
          <button type="submit">Submit</button>
        </Form>
      </Formik>
    </div>
  );
}

export default App;
