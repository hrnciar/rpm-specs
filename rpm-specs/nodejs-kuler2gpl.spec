%{?nodejs_find_provides_and_requires}

%global packagename kuler2gpl
%global enable_tests 1

Name:		nodejs-kuler2gpl
Version:	0.0.6
Release:	6%{?dist}
Summary:	Converts Kuler ASE files to GIMP / Inkscape GPL color palette files

License:	MIT
URL:		https://github.com/myrtleTree33/kuler2gpl
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging

%description
Converts Kuler ASE files to GIMP / Inkscape GPL color palette files.


%prep
%autosetup -n package

sed -i '/grunt-bump/d' package.json

# fix interpreter in main.js
sed -i '1s/env //' bin/main.js

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/main.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}/bin/main.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/main.js \
    %{buildroot}%{_bindir}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[102m -=#=- This package contains no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md doc/
%license LICENSE
%{nodejs_sitelib}/%{packagename}
%{_bindir}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Apr 21 2017 Jared Smith <jsmith@fedoraproject.org> - 0.0.6-1
- Initial packaging
