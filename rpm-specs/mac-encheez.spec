%global commit0 8f11e8aa9fb5a71292bf13939459f2bb37caae89
%global user0 brouhaha

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           mac-encheez
Version:        0.1
Release:        0.6.20170314git%{shortcommit0}%{?dist}
Summary:        Run a program with a modified view of network MAC addresses
License:        GPLv3
URL:            https://github.com/%{user0}/%{name}
Source0:        https://github.com/%{user0}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
%description
mac-encheez provides a way to run a program such that it has a modified view
of the MAC addresses of the network interfaces of the computer.

%prep
%setup -q -n %{name}-%{commit0}

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_libdir}
make install PREFIX="%{_prefix}" LIBDIR="%{_libdir}" DESTDIR="%{buildroot}"

%files
%license gpl-3.0.txt
%doc README.md
%{_libdir}/libfakemac.so
%{_bindir}/encheez

# rpmlint will complain about libfakemac.so having "no-soname".  Since
# this shared library is a preload only, and no other programs are intended
# to be explictly linked to it, there is no point in versioning it.

# rpmlint will complain that the libfakemac.so shared-lib-calls-exit.
# The shared library will only call exit from its initialization function
# if there is an error condition preventing it from functioning, in which
# case exiting is the correct behavior. It would be undesirable to allow
# execution of the target program to commence if the preload is used but
# can't be initialized, as the entire purpose is to alter the execution
# environment.

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20170314git8f11e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.20170314git8f11e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20170314git8f11e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.3.20170314git8f11e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.2.20170314git8f11e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Mar 14 2017 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.1.20170314git8f11e8a
- Initial version.
