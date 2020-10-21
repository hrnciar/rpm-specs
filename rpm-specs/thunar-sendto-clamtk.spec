Name: thunar-sendto-clamtk
Version: 0.06
Release: 7%{dist}
Summary: Simple virus scanning extension for Thunar
License: GPL+ or Artistic 2.0
URL: https://bitbucket.org/davem_/thunar-sendto-clamtk

Source: https://bitbucket.org/davem_/thunar-sendto-clamtk/downloads/thunar-sendto-clamtk-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: Thunar, clamtk >= 5.00

%description
This is a simple extension to add virus scanning to Thunar
in the send-to menu.

ClamTk is a front-end for ClamAV.
It is meant to be lightweight and easy to use.

%prep
%setup -q

%build

%install

desktop-file-install --vendor "" \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/Thunar/sendto \
	%{name}.desktop

%files
%doc CHANGES DISCLAIMER LICENSE README
%{_datadir}/Thunar/sendto/%{name}.desktop

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Dave M. <dave.nerd@gmail.com> - 0.06-1
- Update to 0.06.
- Update URLs.
- Change compression gz -> xz.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Dave M. <dave.nerd@gmail.com> - 0.05-1
- Update to 0.05.

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 0.04-3
- Spec improvements (BZ #1028780).

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 0.04-2
- First version for Fedora.

* Sun Nov 10 2013 Dave M. <dave.nerd@gmail.com> - 0.04-1.fc
- Update to 0.04.
- Minor spec clean-up.
- Updated Url and Source.
- Updated License field.

* Fri Apr 20 2012 Dave M. <dave.nerd@gmail.com> - 0.03-1.fc
- Update to 0.03.

* Fri Aug 12 2011 Dave M. <dave.nerd@gmail.com> - 0.02-1.fc
- Update to 0.02.

* Sat Jul 3 2010 Dave M. <dave.nerd@gmail.com> - 0.01-1.fc
- Initial release 0.01.
