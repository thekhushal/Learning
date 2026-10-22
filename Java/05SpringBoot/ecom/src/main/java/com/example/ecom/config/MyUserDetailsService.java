// package com.example.ecom.config;
// import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.security.core.userdetails.UserDetails;
// import org.springframework.security.core.userdetails.UserDetailsService;
// import org.springframework.security.core.userdetails.UsernameNotFoundException;
// import org.springframework.stereotype.Service;

// import com.example.ecom.User;
// import com.example.ecom.UserPrincipal;
// import com.example.ecom.repository.UserRepository;

// @Service 
// public class MyUserDetailsService implements UserDetailsService {

//     @Autowired
//     UserRepository userRepository;

//     @Override
//     public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
//         User user = userRepository.loadUserByUsername(username);
//         if (user == null) {
//             throw new UsernameNotFoundException("User not found with username: " + username);
//         }
//         return new UserPrincipal(user);
//     }

    
// }
