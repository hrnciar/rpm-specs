%global release_date 20170125
%global theme_name Mistral-Thin

Name:           openbox-theme-mistral-thin
Version:        0
Release:        8.%{release_date}%{?dist}
Summary:        Mistral Thin theme for Openbox

# No license file included, CC-BY-SA mentioned on URL
License:        CC-BY-SA
URL:            https://www.box-look.org/p/1169127/
Source0:        https://dl.opendesktop.org/api/files/download/id/1485351121/%{theme_name}.obt

Requires:       openbox

BuildArch:      noarch

%description
Mistral Thin theme for the Openbox window manager.

%prep
%setup -qc

%build
# nothing to build here

%install
%{__mkdir_p} %{buildroot}/%{_datadir}/themes
%{__cp} -av %{theme_name} %{buildroot}/%{_datadir}/themes

%files
%{_datadir}/themes/%{theme_name}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20170125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Christian Dersch <lupinix@mailbox.org> - 0-1.20170125
- initial packaging effort (rhbz #1440819)
