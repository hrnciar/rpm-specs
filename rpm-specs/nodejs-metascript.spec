%{?nodejs_find_provides_and_requires}

%global packagename metascript
%global enable_tests 1

Name:		nodejs-metascript
Version:	1.0.0
Release:	11%{?dist}
Summary:	Sophisticated meta programming in JavaScript

License:	ASL 2.0
URL:		https://github.com/dcodeIO/MetaScript.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
# nothing
%endif

%description
Sophisticated meta programming in JavaScript, e.g. to build different versions
of a library from a single source tree.


%prep
%setup -q -n package

%nodejs_fixdep ascli
%nodejs_fixdep glob

# Fix interpreters
sed -i '1!b;s/env node/node/' bin/metac
sed -i '1!b;s/env node/node/' bin/metascript

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/metac %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/metac
install -p -D -m0755 bin/metascript %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/metascript

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/metac \
    %{buildroot}%{_bindir}/metac
ln -sf %{nodejs_sitelib}/%{packagename}/bin/metascript \
    %{buildroot}%{_bindir}/metascript


%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%__nodejs tests/test.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md docs/ *.jpg *.png
%license LICENSE
%{nodejs_sitelib}/%{packagename}
%{_bindir}/metac
%{_bindir}/metascript



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 06 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Update script interpreters on scripts in bin/ directory

* Mon Nov 16 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
