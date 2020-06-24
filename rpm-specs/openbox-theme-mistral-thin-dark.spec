%global release_date 20170201
%global theme_name Mistral-Thin-Dark

Name:           openbox-theme-mistral-thin-dark
Version:        0
Release:        7.%{release_date}%{?dist}
Summary:        Mistral Dark theme for Openbox

# No license file included, CC-BY-SA mentioned on URL
License:        CC-BY-SA
URL:            https://www.box-look.org/p/1169703/
Source0:        https://dl.opendesktop.org/api/files/download/id/1485941697/%{theme_name}.obt

Requires:       openbox

BuildArch:      noarch

%description
Mistral Thin theme for the Openbox window manager, dark variant.

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20170201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20170201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20170201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20170201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20170201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20170201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Christian Dersch <lupinix@mailbox.org> - 0-1.20170201
- initial packaging effort (review rhbz #1440822)
