'use client';

import { authService } from '@/libs/auth';
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
      fullName: '',
      email: '',
      password: '',
      dateOfBirth: ''
    },
    onSubmit: async (values, { setSubmitting }): Promise<void> => {
      setSubmitting(true);
      const result = await authService.signUp(values);

      toast({
        title: 'Account created.',
        description: `Hey, ${result.fullName}. We've created your account for you.`,
        status: 'info',
        duration: 3000,
        isClosable: true,
      });
      formik.handleReset('');
      replace('/');
    },
    validationSchema: Yup.object({
      fullName: Yup.string().required('Full Name cannot be empty'),
      dateOfBirth: Yup.string().required('Date of Birth cannot be empty'),
      email: Yup.string().required('Email Address cannot be empty').email('Looks like this is not an email'),
      password: Yup.string().required('Password cannot be empty')
    }),
    validateOnChange: true
  });

  return (
    <VStack minW={{base: 'full', lg: '45%'}} alignItems='stretch' gap={6}>
      <Text textAlign='center'>Sign up for messenger</Text>
      <form onSubmit={formik.handleSubmit}>
        <FormControl isInvalid={!!(formik.touched.fullName && formik.errors.fullName)} mb={5} color='black'>
          <InputGroup>
            <Input type='text' name="fullName" placeholder="Full name" value={formik.values.fullName} onChange={formik.handleChange} />
            {formik.touched.fullName && formik.errors.fullName}
          </InputGroup>
          {formik.touched.fullName && formik.errors.fullName && <FormErrorMessage>{formik.errors.fullName}</FormErrorMessage>}
        </FormControl>

        <FormControl isInvalid={!!(formik.touched.dateOfBirth && formik.errors.dateOfBirth)} mb={5} color='black'>
          <InputGroup>
            <Input type='date' name="dateOfBirth" value={formik.values.dateOfBirth} onChange={formik.handleChange} />
            {formik.touched.dateOfBirth && formik.errors.dateOfBirth}
          </InputGroup>
          {formik.touched.dateOfBirth && formik.errors.dateOfBirth && <FormErrorMessage>{formik.errors.dateOfBirth}</FormErrorMessage>}
        </FormControl>

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
