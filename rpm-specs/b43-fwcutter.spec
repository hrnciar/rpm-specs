Name:           b43-fwcutter
Version:        019
Release:        17%{?dist}
Summary:        Firmware extraction tool for Broadcom wireless driver

License:        BSD
URL:            http://bues.ch/b43/fwcutter/
Source0:        http://bues.ch/b43/fwcutter/%{name}-%{version}.tar.bz2
Source1:        README.too

BuildRequires:  gcc

%description
This package contains the 'b43-fwcutter' tool which is used to
extract firmware for the Broadcom network devices.

See the README.too file shipped in the package's documentation for
instructions on using this tool.

%prep
%setup -q

cp %{SOURCE1} .

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 b43-fwcutter $RPM_BUILD_ROOT%{_bindir}/b43-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 b43-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/b43-fwcutter
%{_mandir}/man1/*
%license COPYING
%doc README README.too

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 019-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 019-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 019-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 John W. Linville <linville@redhat.com> - 019-14
- Add previously unnecessary BuildRequires for gcc

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 019-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 019-12
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 019-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 019-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 019-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 019-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 019-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Peter Lemenkov <lemenkov@gmail.com> - 019-6
- Spec-file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 019-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 019-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb  4 2015 John W. Linville <linville@redhat.com> - 019-3
- Use %%license instead of %%doc for file containing license information

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 John W. Linville <linville@redhat.com> 019-1
- Update for b43-fwcutter-019
- Fixup bad date in changelog for build 011-3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 018-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 John W. Linville <linville@redhat.com> 018-1
- Update for b43-fwcutter-018

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 John W. Linville <linville@redhat.com> 017-1
- Update for b43-fwcutter-017

* Tue Oct 30 2012 John W. Linville <linville@redhat.com> 016-1
- Update URL and source location

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 John W. Linville <linville@redhat.com> 015-2
- Rename README.Fedora to README.too

* Tue Jan 24 2012 John W. Linville <linville@redhat.com> 015-1
- Update for b43-fwcutter-015

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 014-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 John W. Linville <linville@redhat.com> 014-1
- Update for b43-fwcutter-014
- Remove patch to add COPYING file (now in upstream repository)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 John W. Linville <linville@redhat.com> 013-2
- Add COPYING file

* Mon Apr 19 2010 John W. Linville <linville@redhat.com> 013-1
- Update for b43-fwcutter-013

* Fri Aug 28 2009 Bill Nottingham <notting@redhat.com> 012-2
- Update with some patches from git

* Mon Aug 24 2009 John W. Linville <linville@redhat.com> 012-1
- Update for b43-fwcutter-012

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 011-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 011-5
- Build with $RPM_OPT_FLAGS.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 John W. Linville <linville@redhat.com> 011-3
- Update for b43-fwcutter-011

* Mon Jan 21 2008 John W. Linville <linville@redhat.com> 010-2
- Update for b43-fwcutter-010

* Thu Aug 23 2007 John W. Linville <linville@redhat.com> 008-1
- Import skeleton from bcm43xx-fwcutter-006-3
- Initial build
