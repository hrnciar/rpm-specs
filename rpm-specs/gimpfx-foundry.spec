Name:		gimpfx-foundry
Version:	2.6.1
Release:	13%{?dist}
Summary:	Additional GIMP plugins
License:	GPLv2+ and GPLv3+ and Public Domain
URL:		http://gimpfx-foundry.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-2.6-1.tar.gz
Source1:	%{name}.metainfo.xml
%if 0%{?fedora} >= 21  
BuildRequires:	libappstream-glib
%endif
Requires:	gimp >= 2.6.0
BuildArch:	noarch

%description
These scripts allow GIMP graphics to be endowed with special effects, such as 
blurring or distorting them in certain ways. This package has 117+ new 
scripts for GIMP that are not part of the graphic software's standard 
installation.

Among them are the Roy Lichtenstein effect script to render graphics in the 
pop artist's style, the Planet Render script to create a planet of your 
choosing and desired size and dimension. and the Old Photo script to give 
existing photos that antiquated touch.

%prep
%setup -q -c %{name}-%{version}

%build
## Nothing to build.

%install
install -d %{buildroot}%{_datadir}/gimp/2.0/scripts/
install -m 0644 -p *.scm -t %{buildroot}%{_datadir}/gimp/2.0/scripts/
%if 0%{?fedora} >= 21  
# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%files
%doc release-notes.txt
%{_datadir}/gimp/2.0/scripts/*.scm
%if 0%{?fedora} >= 21  
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Apr 17 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 2.6.1-5
- Renamed spec file for consistency
- Cleaned up for adherance to Fedora Packaging Guideline

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 2.6.1-2
- Added GPLv2+ and Public Domain licenses to License tag

* Wed Jun 03 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> - 2.6.1-1
- Initial version

