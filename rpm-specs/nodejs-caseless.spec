%global enable_tests 1
%global srcname caseless

Name:           nodejs-%{srcname}
Version:        0.11.1
Release:        8%{?dist}
Summary:        Encode and decode streams into string streams
License:        ASL 2.0
URL:            https://github.com/mikeal/caseless
#Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz
# The 0.11.1 release hasn't been put on npmjs.org yet, so we'll pull from github
Source0:	https://github.com/request/%{srcname}/archive/v%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tape)
%endif

%description
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json index.js \
     %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
node test.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Jared Smith <jsmith@fedoraproject.org> - 0.11.1-1
- Update to upstream 0.11.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 25 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.11.0-1
- Initial package
