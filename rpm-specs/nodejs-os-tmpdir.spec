# ava is not in fedora yet
%global enable_tests 0
%global module_name os-tmpdir
%global gittag0 1.0.2

Name:           nodejs-%{module_name}
Version:        %{gittag0}
Release:        8%{?dist}
Summary:        Node.js os.tmpdir() ponyfill

License:        MIT
URL:            https://github.com/sindresorhus/os-tmpdir
Source0:        https://github.com/sindresorhus/%{module_name}/archive/v%{gittag0}.tar.gz#/%{module_name}-%{gittag0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires: npm(ava)
%endif

%description
%{summary}.

%prep
%autosetup -n %{module_name}-%{gittag0}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
node test.js
%endif

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 01 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Update to 1.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Initial packaging

