Summary:   Firmware loader for Qualcomm Gobi WWAN devices 
Name:      gobi_loader
Version:   0.7
Release:   24%{?dist}
License:   GPLv2
Source0:   http://www.codon.org.uk/~mjg59/gobi_loader/download/%{name}-%{version}.tar.gz
URL:       http://www.codon.org.uk/~mjg59/gobi_loader

BuildRequires: gcc

%description
gobi_loader is a firmware loader for Qualcomm Gobi USB chipsets. These
devices appear in an uninitialized state when power is applied and require
firmware to be loaded before they can be used as modems. gobi_loader adds
a udev rule that will trigger loading of the firmware and make the modem
usable.

Note that gobi_loader requires firmware images which can't be freely
redistributed. See http://www.codon.org.uk/~mjg59/gobi_loader for more
information.

%prep
%setup -q
sed -i -e 's|gcc -Wall|gcc %{optflags} %{?__global_ldflags}|' Makefile

%build
make %{?_smp_mflags}

%install
make install prefix=%{buildroot}

%files
%attr(755,root,root) /lib/udev/gobi_loader
%attr(644,root,root) /lib/udev/rules.d/60-gobi.rules
%doc README

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Bojan Smojver <bojan@rexursive.com> 0.7-18
- add gcc build requirement

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.7-12
- Use '|' as delimiter in sed expression to edit Makefile (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Bojan Smojver <bojan@rexursive.com> 0.7-6
- fix bug #869807: actually build with RPM_OPT_FLAGS/RPM_LD_FLAGS

* Tue Oct  9 2012 Bojan Smojver <bojan@rexursive.com> 0.7-5
- Do not mix macro and variable style
- Removed obsolete stuff (no plans to support EPEL5 at this point)

* Mon Jul 16 2012 Bojan Smojver <bojan@rexursive.com> 0.7-4
- Include README file

* Mon Sep 12 2011 Bojan Smojver <bojan@rexursive.com> 0.7-3
- Obey RPM_OPT_FLAGS

* Wed Sep  7 2011 Bojan Smojver <bojan@rexursive.com> 0.7-2
- Clean up spec a bit for review

* Mon Aug  2 2010 Matthew Garrett <mjg59@fedoraproject.org> 0.7-1
- New upstream release

* Fri Jun  4 2010 Matthew Garrett <mjg59@fedoraproject.org> 0.6-1
- Initial release
