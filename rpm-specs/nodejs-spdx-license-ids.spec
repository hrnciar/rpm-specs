# spec file for package nodejs-nodejs-spdx-license-ids

%global npm_name spdx-license-ids
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
# tests are disabled because they depend on a newer version of nodejs

Name:		nodejs-spdx-license-ids
Version:	1.2.0
Release:	11%{?dist}
Summary:	A list of SPDX license identifiers
Url:		https://github.com/shinnn/spdx-license-ids
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:	https://spdx.org/licenses/licenses.json
# The list in this package is built from the list at spdx.org, but
# unfortunately the build instructions for this package depend on a newer
# version of nodejs and on direct network access, so we'll have to come up
# with our own way of building the list using tools already in Fedora
Source2:	https://raw.githubusercontent.com/shinnn/spdx-license-ids/v1.2.0/test.js
# the test file is not included in the NPM package

License:	Unlicense
# Yes, this is the "Unlicense" license

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	jq
BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(rimraf)
BuildRequires:	npm(tape)
%endif

%description
A list of SPDX license identifiers

%prep
%setup -q -n package
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

chmod -x README.md

# Remove the generated file and rebuild from source as part of the %%build step
rm spdx-license-ids.json

%build
# Use the jq tool to rebuild the list from the source file, rather than using
# the upstream method of running 'build.js', because 'build.js' depends on a
# newer version of nodejs and also requires network connectivity.
%{_bindir}/jq '[.licenses[].licenseId] | map(select(endswith("+")|not))' licenses.json > spdx-license-ids.json

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json spdx-license-ids.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%check
%{nodejs_symlink_deps} --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} --harmony_arrow_functions test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%{nodejs_sitelib}/spdx-license-ids
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Jared Smith <jsmith@fedoraproject.org> - 1.2.0-3
- Update to upstream 1.2.0 release
- Rebuild from source using the jq utility

* Wed Jun 10 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
