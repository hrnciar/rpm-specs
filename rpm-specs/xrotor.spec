Name:           xrotor
Version:        7.55
Release:        17%{?dist}
Summary:        Design and analysis tools for propellers and windmills

# Plotlib is LGPLv2+, the rest is GPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://web.mit.edu/drela/Public/web/xrotor/
Source0:        http://web.mit.edu/drela/Public/web/xrotor/Xrotor%{version}.tar.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL
# Makefile variables and flags
Patch0:         Xrotor7.55-makefile.patch

BuildRequires:  gcc-gfortran libX11-devel
Requires:       xorg-x11-fonts-misc


%description
XROTOR is an interactive program for the design and analysis of propellers
and windmills. It includes
 1. Design of minimum induced loss rotor (propeller or windmill)
 2. Prompted input of an arbitrary rotor geometry
 3. Interactive modification of a rotor geometry
and many others.


%prep
%autosetup -p1 -n Xrotor
cp %{SOURCE1} .
cp %{SOURCE2} .


%build
export FFLAGS="-fallow-argument-mismatch %{optflags}"
export CFLAGS="%{optflags}"

%make_build -C plotlib
%make_build -C bin


%install
%make_install -C bin BINDIR=%{_bindir}


%files
%doc version_notes.txt xrotor_doc.txt
%license LICENSE.GPL LICENSE.LGPL
%{_bindir}/xrotor
%{_bindir}/jplot
%{_bindir}/jplote


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 7.55-9
- Rebuild (gfortran)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.55-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.55-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.55-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Sandro Mani <manisandro@gmail.com> - 7.55-4
- Build without -fdefault-real-8

* Fri Sep 13 2013 Sandro Mani <manisandro@gmail.com> - 7.55-3
- Fix license

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 7.55-2
- Add license file

* Thu Sep 12 2013 Sandro Mani <manisandro@gmail.com> - 7.55-1
- Initial package for review
