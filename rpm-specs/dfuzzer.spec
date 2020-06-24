Name:           dfuzzer
Version:        1.4
Release:        11%{?dist}
Summary:        D-Bus fuzz testing tool

%global commit 884972e7f115bf22121328803af2910cd16c4c20
%global shortcommit %(c=%{commit}; echo ${c:0:7})

License:        GPLv3+
URL:            https://github.com/matusmarhefka/dfuzzer

# GitHub generates different links from names of downloaded packages, therefore you must run
# this command before rpmbuild (it downloads tarball, renames it and moves to the SOURCES):
# spectool -g dfuzzer.spec; mv *.tar.gz ../SOURCES/
Source0:        https://github.com/matusmarhefka/dfuzzer/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  gcc
BuildRequires:  glib2-devel, libffi-devel, doxygen


%description
Tool for fuzz testing processes communicating through D-Bus. It can be
used to test processes connected to both, the session bus and the system
bus daemon. Dfuzzer works as a client, it first connects to the bus
daemon and then it traverses and fuzz tests all the methods provided
by a D-Bus service.


%prep
%setup -qn %{name}-%{commit}


%build
cd ./src
make %{?_smp_mflags} CFLAGS="%{optflags} `pkg-config --cflags --libs gio-2.0 libffi`"
make doc
cd ../


%install
mkdir -p  %{buildroot}%{_bindir}
install -pm 0755 src/dfuzzer %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 man/dfuzzer.1 %{buildroot}%{_mandir}/man1/dfuzzer.1
mkdir -p %{buildroot}%{_sysconfdir}/
install -pm 0644 src/dfuzzer.conf %{buildroot}%{_sysconfdir}/dfuzzer.conf


%files
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/*
%{_mandir}/man1/dfuzzer.1*
%doc README.md ChangeLog COPYING doc/*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 19 2015 Matus Marhefka <mmarhefk@redhat.com> 1.4-1
- Initial version of the package
