%{?nodejs_find_provides_and_requires}

%global packagename linefix
%global enable_tests 1

Name:		nodejs-linefix
Version:	0.1.1
Release:	9%{?dist}
Summary:	Recursively repair line endings

License:	MIT
URL:		https://github.com/jhoff/linefix
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/jhoff/linefix/master/LICENSE.txt


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging

%description
Recursively repair line endings


%prep
%autosetup -n package
cp -p %{SOURCE1} .

# fix script interpreter not to use env
sed -i '1!b;s/env node/node/' bin/fix.js

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json bin/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/fix.js %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/fix.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/fix.js \
    %{buildroot}%{_bindir}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[103m -=#=- No test suite -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE.txt
%{nodejs_sitelib}/%{packagename}
%{_bindir}/linefix

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 11 2016 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-3
- Fix silly copy/paste error

* Tue Aug 09 2016 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-2
- Create linefix executable

* Sat Jul 30 2016 Jared Smith <jsmith@fedoraproject.org> - 0.1.1-1
- Initial packaging
