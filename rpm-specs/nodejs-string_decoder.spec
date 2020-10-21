# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

# Tests are disabled.  We could run them, but they are not shipped with tar.
%global enable_tests 0
%global barename string_decoder

Name:               nodejs-string_decoder
Version:            0.10.31
Release:            12%{?dist}
Summary:            The string_decoder module from Node core

License:            MIT
URL:                https://www.npmjs.org/package/string_decoder
Source0:            http://registry.npmjs.org/string_decoder/-/string_decoder-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora}
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(tap)
%endif


%description
The string_decoder module from Node core.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/string_decoder
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/string_decoder

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
tap test/simple/*.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/string_decoder/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Ralph Bean <rbean@redhat.com> - 0.10.31-2
- Process feedback from package review.
- Remove Group tag.
- Remove '19' from fedora conditional.
- Use %%license macro for LICENSE
- Disable tests, since they're not shipped with the tarball.

* Wed May 20 2015 Ralph Bean <rbean@redhat.com> - 0.10.31-1
- Initial packaging for Fedora.
