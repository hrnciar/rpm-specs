Name:           pam_2fa
Version:        1.0
Release:        5%{?dist}
Summary:        Second factor authentication for PAM

License:        GPLv3+
URL:            https://cern-cert.github.io/pam_2fa/
Source0:        https://github.com/CERN-CERT/pam_2fa/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  curl-devel
BuildRequires:  openldap-devel
BuildRequires:  ykclient-devel
BuildRequires:  automake
BuildRequires:  libtool
Requires:       pam

%description
The PAM 2FA module provides a second factor authentication, which can be
combined with the standard PAM-based password authentication to ask for:

 *  What you know: user account password ( standard PAM modules )
 *  What you have (pick one of): (PAM 2FA)

 *  A Google Authenticator Application on your phone
 *  A Phone Number capable of receiving SMS
 *  A Yubikey


%package -n pam_ssh_user_auth
Summary:        PAM module to help with %{!?el7:SSH_AUTH_INFO_0}%{?el7:SSH_USER_AUTH}
Requires:       pam

%description -n pam_ssh_user_auth
pam_ssh_user_auth checks the value of %{!?el7:SSH_AUTH_INFO_0}%{?el7:SSH_USER_AUTH} and will return success
if is non-empty and failure if it is.  It can be used to skip other PAM
authentication methods with a configuration like:

auth       [success=1 ignore=ignore default=die] pam_ssh_user_auth.so
auth       substack     password-auth


%prep
%setup -q
%{!?el7:sed -i -e s/SSH_USER_AUTH/SSH_AUTH_INFO_0/ *.c}

%build
autoreconf -i
%configure --libdir=/%{_lib} \
           --with-pam-dir=/%{_lib}/security/
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
/%{_lib}/security/pam_2fa.so

%files -n pam_ssh_user_auth
%license COPYING
%doc README.md
/%{_lib}/security/pam_ssh_user_auth.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Orion Poplawski <orion@nwra.com> - 1.0-2
- Use openssh's upstream SSH_AUTH_INFO_0 except on EL7

* Fri Nov 16 2018 Orion Poplawski <orion@nwra.com> - 1.0-1
- Initial package
