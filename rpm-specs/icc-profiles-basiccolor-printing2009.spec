Name:           icc-profiles-basiccolor-printing2009
Version:        1.2.0
Release:        14%{?dist}
Summary:        The OpenICC profiles from basICColor

License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/basICColor-Profiles/%{name}-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  color-filesystem
Requires:       color-filesystem
#Owns %%{_icccolordir}/basICColor
Requires:       icc-profiles-openicc



%description
Printing profiles according to ISO 12647-2. These are CMYK
ICC profiles for ISO Printing conditions.


%prep
%setup -q


%build
%configure --enable-verbose
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT



%files
%doc AUTHORS ChangeLog COPYING
%{_icccolordir}/basICColor/ISOcoated_v2_300_bas.ICC
%{_icccolordir}/basICColor/ISOcoated_v2_bas.ICC
%{_icccolordir}/basICColor/ISOcoated_v2_grey1c_bas.ICC
%{_icccolordir}/basICColor/ISOnewspaper_v4_26_bas.ICC
%{_icccolordir}/basICColor/ISOuncoatedyellowish_bas.ICC
%{_icccolordir}/basICColor/PSO_Coated_300_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_Coated_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_LWC_Improved_bas.ICC
%{_icccolordir}/basICColor/PSO_LWC_Standard_bas.ICC
%{_icccolordir}/basICColor/PSO_MFC_Paper_bas.ICC
%{_icccolordir}/basICColor/PSO_SNP_Paper_bas.ICC
%{_icccolordir}/basICColor/PSO_Uncoated_ISO12647_bas.ICC
%{_icccolordir}/basICColor/PSO_Uncoated_NPscreen_ISO12647_bas.ICC
%{_icccolordir}/basICColor/SC_paper_bas.ICC


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- Initial release
