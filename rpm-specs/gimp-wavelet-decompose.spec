%global		addon wavelet-decompose

Name:		gimp-%{addon}
Version:	0
Release:	7%{?dist}
Summary:	Decomposing image plug-in for Gimp
License:	GPLv3+
URL:		http://registry.gimp.org/node/13549
Source0:	http://registry.gimp.org/files/%{addon}.scm
Source1:	%{name}.metainfo.xml
Source2:	license.txt
BuildRequires:	libappstream-glib
Requires:	gimp
BuildArch:	noarch

%description
Script-Fu script for lossless decomposing an image into different 
detail scales useful for photo post processing (for instance 
repairing skin in portraits).

%prep
# Copy license
cp -p %{SOURCE2} .

%build
## Nothing to build.

%install
install -Dpm 0644 %{SOURCE0} -t %{buildroot}%{_datadir}/gimp/2.0/scripts/
# Add AppStream metadata
install -Dpm 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/metainfo/

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license license.txt
%{_datadir}/gimp/2.0/scripts/*.scm
%{_datadir}/metainfo/%{name}.metainfo.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Luya Tshimbalanga <luy@fedoraproject.org> - 0-1
- Initial package
