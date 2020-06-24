%global srcname grunt-known-options

Name:           nodejs-%{srcname}
Version:        1.1.1
Release:        3%{?dist}
Summary:        The known options used in Grunt
License:        MIT
URL:            https://www.npmjs.com/package/grunt-known-options
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch

ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
%{summary}.

%prep
%autosetup -n package

%build
#nothing to do

%check
%{__nodejs} -e 'require("./")'

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}

cp -pr package.json *.js \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Jan Staněk <jstanek@redhat.com> - 1.1.1-1
- Upgrade to version 1.1.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.1.0-1
- Initial package
