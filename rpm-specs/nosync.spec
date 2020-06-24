Name:           nosync
Version:        1.1
Release:        8%{?dist}
Summary:        Preload library for disabling file's content synchronization
License:        ASL 2.0
URL:            http://github.com/kjn/%{name}
Source0:        http://github.com/kjn/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Eliminate dependency on ELF constructor ordering
# Solves segfaults during buildroot population in mock with nosync
# enabled for builds with openssl
# "FIPS module installed state definition is modified" changes
# https://bugzilla.redhat.com/show_bug.cgi?id=1837809
# https://github.com/kjn/nosync/pull/4
Patch0:         4.patch

BuildRequires:  make
BuildRequires:  gcc

%description
nosync is a small preload library that can be used to disable
synchronization of file's content with storage devices on GNU/Linux.
It works by overriding implementations of certain standard functions
like fsync or open.

%prep
%autosetup -p1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%makeinstall

%files
%doc AUTHORS README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%{_libdir}/%{name}

%changelog
* Wed May 20 2020 Adam Williamson <awilliam@redhat.com> - 1.1-8
- Backport PR #4 from Florian Weimer to fix RHBZ #1837809

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 1.1-3
- Add BR on gcc and make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 21 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-4
- Update to current packaging guidelines

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul  5 2014 Mikolaj Izdebski <zurgunt@gmail.com> - 1.0-1
- Initial packaging
