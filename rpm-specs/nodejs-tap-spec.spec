%{?nodejs_find_provides_and_requires}

%global packagename tap-spec
%global enable_tests 1

Name:		nodejs-tap-spec
Version:	4.1.1
Release:	6%{?dist}
Summary:	Formatted TAP output like Mocha's spec reporter

License:	MIT
URL:		https://github.com/scottcorgan/tap-spec.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# No license file upstream, requested at https://github.com/scottcorgan/tap-spec/issues/46
Source1:	LICENSE-MIT.txt

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(chalk)
BuildRequires:	npm(duplexer)
BuildRequires:	npm(figures)
BuildRequires:	npm(lodash)
BuildRequires:	npm(pretty-ms)
BuildRequires:	npm(repeat-string)
BuildRequires:	npm(tap-out)
BuildRequires:	npm(through2)
%if 0%{?enable_tests}
BuildRequires:	npm(tap)
BuildRequires:	npm(tapes)
%endif

%description
Formatted TAP output like Mocha's spec reporter


%prep
%setup -q -n package
# copy the license file
cp -p %{SOURCE1} .

sed -i '1s/env //' bin/cmd.js

%nodejs_fixdep tap-out

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/cmd.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}/bin/cmd.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/cmd.js \
    %{buildroot}%{_bindir}/tap-spec

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# see package.json
%{_bindir}/tap test/**/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"

%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-MIT.txt
%{nodejs_sitelib}/%{packagename}
%{_bindir}/tap-spec


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 23 2016 Jared Smith <jsmith@fedoraproject.org> - 4.1.1-1
- Initial packaging
