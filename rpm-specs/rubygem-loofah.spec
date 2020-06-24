%global gem_name loofah

Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 1%{?dist}
Summary: Manipulate and transform HTML/XML documents and fragments
License: MIT
URL: https://github.com/flavorjones/loofah
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(nokogiri) >= 1.6.6.2
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rr)
BuildRequires: rubygem(crass)
BuildArch: noarch

%description
Loofah is a general library for manipulating and transforming HTML/XML
documents and fragments, built on top of Nokogiri.
Loofah excels at HTML sanitization (XSS prevention). It includes some nice
HTML sanitizers, which are based on HTML5lib's safelist, so it most likely
won't make your codes less secure. (These statements have not been evaluated
by Netexperts.)


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
ruby -Itest -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/benchmark
%{gem_instdir}/test

%changelog
* Fri Feb 21 2020 Vít Ondruch <vondruch@redhat.com> - 2.4.0-1
- Update to Loofah 2.4.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Pavel Valena <pvalena@redhat.com> - 2.3.1-1
- Update to loofah 2.3.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Vít Ondruch <vondruch@redhat.com> - 2.2.3-1
- Update to Loofah 2.2.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Pavel Valena <pvalena@redhat.com> - 2.2.2-1
- Update to loofah 2.2.2.
  Resolves: CVE-2018-8048

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.0.3-1
- Update to loofah 2.0.3 (rhbz#1256165)
- Use %%autosetup macro
- Drop macros for Fedora 20 (it is now EOL)
- Drop unneeded %%license definition

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.0.2-1
- Update to loofah 2.0.2 (rhbz#1218819)
- Drop patch to skip failing test (it works now, with Nokogiri 1.6.6.2)
- Drop Fedora 19 support
- Use %%license macro

* Thu Sep 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.0.1-1
- Update to loofah 2.0.1 (RHBZ #1132898)
- Drop upstreamed RR patch

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.0.0-1
- Update to loofah 2.0.0 (RHBZ #1096760)
- Adjustments for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sat Dec 28 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.2.1-1
- Initial package
