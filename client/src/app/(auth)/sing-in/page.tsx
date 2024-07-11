'use client';

import {
  Button,
  FormControl,
  FormErrorMessage,
  Input,
  InputGroup,
  Text,
  VStack,
  useToast,
} from '@chakra-ui/react';
import { useFormik } from 'formik';
import { useRouter } from 'next/navigation';
import * as Yup from 'yup';

export default function SignUp() {
  const { replace } = useRouter();
  const toast = useToast();

  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
    },
    onSubmit: values => {
      toast({
        title: 'Account created.',
        description: `Hey, ${values.email}. You successfully logged in.`,
        status: 'info',
        duration: 3000,
        isClosable: true,
      });
      formik.handleReset('');
      replace('/');
    },
    validationSchema: Yup.object({
      email: Yup.string().required('Email Address cannot be empty').email('Looks like this is not an email'),
      password: Yup.string().required('Password cannot be empty')
    }),
    validateOnChange: true
  });

  console.log('render');

  return (
    <VStack minW={{base: 'full', lg: '45%'}} alignItems='stretch' gap={6}>
      <Text textAlign='center'>Login in to messenger</Text>
      <form onSubmit={formik.handleSubmit}>
        <FormControl isInvalid={!!(formik.touched.email && formik.errors.email)} mb={5} color='black'>
          <InputGroup>
            <Input type='text' name="email" placeholder="Email" value={formik.values.email} onChange={formik.handleChange} />
            {formik.touched.email && formik.errors.email}
          </InputGroup>
          {formik.touched.email && formik.errors.email && <FormErrorMessage>{formik.errors.email}</FormErrorMessage>}
        </FormControl>

        <FormControl isInvalid={!!(formik.touched.password && formik.errors.password)} mb={5} color='black'>
          <InputGroup>
            <Input type='password' name="password" placeholder="Password" value={formik.values.password} onChange={formik.handleChange} />
            {formik.touched.password && formik.errors.password}
          </InputGroup>
          {formik.touched.password && formik.errors.password && <FormErrorMessage>{formik.errors.password}</FormErrorMessage>}
        </FormControl>

        <Button
          type='submit'
          w='full'
          textTransform='uppercase'
          _hover={{ filter: 'brightness(0.9)' }}
        >
          Create Account
        </Button>
      </form>
    </VStack>
  );
}
