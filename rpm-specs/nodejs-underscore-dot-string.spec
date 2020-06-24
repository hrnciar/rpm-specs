%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%if 0%{?fedora}
%global enable_minify 1
%endif

Name:       nodejs-underscore-dot-string
Version:    2.3.1
Release:    14%{?dist}
Summary:    String manipulation extensions for the Underscore.js JavaScript library
# License text is contained within README.markdown.
License:    MIT
URL:        https://github.com/epeli/underscore.string
Source0:    http://registry.npmjs.org/underscore.string/-/underscore.string-%{version}.tgz
BuildArch:  noarch

# Building fails due to incorrectly determined file encoding.
# Pull request sent: https://github.com/epeli/underscore.string/pull/210
Patch0:     %{name}-2.3.1-Ensure-correct-encoding.patch

BuildRequires:  nodejs-devel

%if 0%{?enable_minify}
BuildRequires:  rubygem-rake
BuildRequires:  rubygem-uglifier
BuildRequires:  rubygem-json
%endif

%if 0%{?enable_tests}
BuildRequires:  npm(qunit)
BuildRequires:  phantomjs
%endif

%description
%{summary}.


%prep
%setup -q -n package
%patch0 -p1
# Pre-minified files must be removed and minified manually.
rm -f dist/*


%build
%if 0%{?enable_minify}
/usr/bin/rake build
%endif


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/underscore.string
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/underscore.string

%if 0%{?enable_minify}
cp -pr dist/ \
    %{buildroot}%{nodejs_sitelib}/underscore.string
%endif

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
ln -sf %{nodejs_sitelib} .
%endif


%files
%doc README.markdown
%{nodejs_sitelib}/underscore.string


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.3.1-7
- Add missing BuildRequires on rubygems-json

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.3.1-3
- conditionalize minification; disable on EPEL due to missing deps

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.1-1
- initial package
