Name:		fs_mark
Version:	3.3
Release:	22%{?dist}
Summary:	Benchmark synchronous/async file creation

License:	GPLv2+
URL:		http://sourceforge.net/projects/fsmark/
Source0:	http://downloads.sourceforge.net/fsmark/%{name}.tgz

BuildRequires:	gcc

Patch0:		nostatic

%description
The fs_mark program is meant to give a low level bashing to file
systems. The write pattern that we concentrate on is heavily
synchronous IO across mutiple directories, drives, etc.


%prep
%setup -q -n fs_mark
%patch0 -p1 

%build
CFLAGS="$RPM_OPT_FLAGS" make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -D fs_mark $RPM_BUILD_ROOT/usr/bin/fs_mark


%files
%doc README plot_test
%{_bindir}/fs_mark


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Eric Sandeen <sandeen@redhat.com> - 3.3-18
- Add BuildRequires: gcc (#1604010)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 08 2008 Eric Sandeen <sandeen@redhat.com> 3.3-1
- New upstream release

* Fri Jul 18 2008 Eric Sandeen <sandeen@redhat.com> 3.2-3
- Updated tarball from new sf.net home

* Wed Jun 18 2008 Eric Sandeen <sandeen@redhat.com> 3.2-2
- Address review comments

* Mon Jun 09 2008 Eric Sandeen <sandeen@redhat.com> 3.2-1
- Initial build
