%{?nodejs_find_provides_and_requires}

%global packagename faucet
%global enable_tests 1

Name:		nodejs-faucet
Version:	0.0.1
Release:	6%{?dist}
Summary:	Human-readable TAP summarizer

License:	MIT
URL:		https://github.com/substack/faucet.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The example files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	examples-%{version}.tar.bz2
Source10:	dl-tests.sh
# The license file is upstream, but not in the npm tarball.
Source20:	https://raw.githubusercontent.com/substack/faucet/0.0.1/LICENSE


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(tap-parser)
BuildRequires:	npm(through2)
%if 0%{?enable_tests}
BuildRequires:	npm(duplexer)
BuildRequires:	npm(sprintf)
%endif

%description
A human-readable TAP summarizer.


%prep
%setup -q -n package
# setup the examples
%setup -q -T -D -a 1 -n package
# copy the LICENSE file
cp -p %{SOURCE20} .

sed -i '1s/env //' bin/cmd.js

%nodejs_fixdep defined
%nodejs_fixdep minimist
%nodejs_fixdep tap-parser
%nodejs_fixdep tape
%nodejs_fixdep through2

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/cmd.js %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/cmd.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/cmd.js \
    %{buildroot}%{_bindir}/faucet


%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[102m -=#=- This package has no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.markdown example/
%license LICENSE
%{nodejs_sitelib}/%{packagename}
%{_bindir}/faucet


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb  3 2016 Jared Smith <jsmith@fedoraproject.org> - 0.0.1-1
- Initial packaging
