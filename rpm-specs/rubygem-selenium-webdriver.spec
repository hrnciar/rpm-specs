%global gem_name selenium-webdriver

%global spec_version 3.141.59

Summary: The next generation developer focused tool for automated testing of webapps
Name: rubygem-%{gem_name}
Version: 3.142.7
Release: 3%{?dist}
License: ASL 2.0
URL: https://github.com/SeleniumHQ/selenium/wiki/Ruby-Bindings
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Not all releases are tagged, let's use the last tag
# https://github.com/SeleniumHQ/selenium/issues/8039
# The tests are not shipped with the gem; you can get them like so:
# git clone https://github.com/SeleniumHQ/selenium --no-checkout
# cd selenium && git archive -v -o selenium-webdriver-3.141.59-spec.txz selenium-3.141.59 rb/spec rb/lib/selenium/webdriver/phantomjs{/,.rb}

Source1: %{gem_name}-%{spec_version}-spec.txz

BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(childprocess)
BuildRequires: rubygem(rubyzip)
BuildRequires: rubygem(rack)
BuildRequires: ruby
# Is needed even by unit tests
BuildRequires: %{_bindir}/firefox
# Firefox is no available on armv7hl
# https://bugzilla.redhat.com/show_bug.cgi?id=1839833
ExcludeArch: armv7hl
BuildArch: noarch

%description
WebDriver is a tool for writing automated tests of websites. It aims to mimic
the behavior of a real user, and as such interacts with the HTML of the
application.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -n %{gem_name}-%{version} -b1

# We have newer version in Fedora
# https://github.com/SeleniumHQ/selenium/pull/8592
%gemspec_remove_dep -g childprocess ["< 4.0"]
%gemspec_add_dep -g childprocess ["< 5.0"]

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/firefox/native/linux/x86/x_ignore_nofocus.so
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/firefox/native/linux/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/ie/native/x64/IEDriver.dll
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/ie/native/win32/IEDriver.dll

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/rb/spec .

# No need run tests for IE, Edge or Safari
rm -rf spec/unit/selenium/webdriver/{ie,safari,edge}

# Phantomjs does not seem to be shipped
rm -rf spec/unit/selenium/webdriver/phantomjs/

# I was unable to run integration tests (requires FF or chrome)
rm -rf spec/integration

# We expect failures due to older test suite, and missing java
rspec -Ilib:%{_builddir}/rb/lib spec \
  | tee -a /dev/stderr | grep -q "examples, 18 failures, "
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec


%changelog
* Fri Jul 31 14:13:22 GMT 2020 Pavel Valena <pvalena@redhat.com> - 3.142.7-3
- Relax Childprocess dependency.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.142.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Pavel Valena <pvalena@redhat.com> - 3.142.7-1
- Update to selenium-webdriver 3.142.7.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Vít Ondruch <vondruch@redhat.com> - 2.45.0-12
- Relax rubyzip dependency.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Vít Ondruch <vondruch@redhat.com> - 2.45.0-10
- Relax childprocess dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Mo Morsi <mmorsi@redhat.com> - 2.45.0-2
- Fix dependencies

* Thu Apr 09 2015 Mo Morsi <mmorsi@redhat.com> - 2.45.0-1
- Update to 2.45.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.3.2-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 2.3.2-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 2.3.2-1
- Initial package
