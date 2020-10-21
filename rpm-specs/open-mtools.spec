%global tarname mtools
Name:       open-%{tarname}
Version:    1.0
Release:    15%{?dist}
Summary:    Tools for testing IP multicast
# README.txt:           Public Domain
# mpong.c:              BSD
# TestNet/docbook.css:  BSD
License:    Public Domain and BSD
URL:        https://marketplace.informatica.com/solutions/informatica_%{tarname}
# The source repository does not exist on Google Code anymore.
# The homepage requires a registration for a download.
# The are some imports on Github like
# <https://github.com/landtuna/open-mtools.
# There also exists similar <https://github.com/troglobit/mtools>.
Source0:    https://%{name}.googlecode.com/files/%{tarname}.%{version}.zip
BuildRequires:  coreutils
BuildRequires:  gcc

%description
This package contains the msend, mdump, and mpong tools to aid in testing
multicast networks.

%prep
%setup -q -n %{tarname}
# Delete precompiled binaries
rm -r AIX-* Darwin-* FreeBSD-* Linux-* SunOS-* Win2k-*
# Fix EOLs
for F in README.txt; do
    tr -d "\r" < "$F" > "${F}.unix"
    touch -r "$F" "${F}.unix"
    mv "${F}.unix" "${F}"
done

%build
for F in *.c; do
    cc %{optflags} %{?__global_ldflags} "$F" -o "${F%.c}" \
        $(test "$F" = 'mpong.c' && printf -- '-lm')
done

%install
install -d %{buildroot}%{_bindir}
for F in *.c; do
    install -t %{buildroot}%{_bindir} "${F%.c}"
done

%files
%doc README.txt TestNet/*
%{_bindir}/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Petr Pisar <ppisar@redhat.com> - 1.0-10
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Petr Pisar <ppisar@redhat.com> - 1.0-1
- 1.0 version packaged
