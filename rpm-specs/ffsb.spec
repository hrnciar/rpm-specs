Name:		ffsb
Version:	6.0
Release:	0.18.rc2%{?dist}
Summary:	The Flexible Filesystem Benchmark

License:	GPLv2+
URL:		http://sourceforge.net/projects/ffsb
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}-rc2.tar.bz2
BuildRequires:	gcc

Patch0:		getu32random.patch


%description
The Flexible Filesystem Benchmark (FFSB) is a cross-platform filesystem
performance measurement tool. It uses customizable profiles to measure
of different workloads, and it supports multiple groups of threads
across multiple filesystems.

%prep
%setup -q -n ffsb-6.0-rc2
%patch0 -p1

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Odd leftover in the tarball...
rm -f examples/profile_smallfile_reads~



%files
%doc AUTHORS COPYING README examples
%{_bindir}/ffsb

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.18.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.17.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.16.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.15.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Eric Sandeen <sandeen@redhat.com> - 6.0-0.14.rc2
- BuildRequires: gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.13.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.11.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 15 2017 Eric Sandeen <sandeen@redhat.com> - 6.0-0.10.rc2
- rename getrandom to getu32random to avoid glibc clash (bz #1422441)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.9.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-0.8.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.7.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.6.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.5.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.4.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.3.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-0.2.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Eric Sandeen <sandeen@redhat.com> 6.0-0.1.rc2
- New(ish) upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Eric Sandeen <sandeen@redhat.com> 5.2.1-1
- Initial build
