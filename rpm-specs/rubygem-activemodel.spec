%global gem_name activemodel

# Circular dependency with rubygem-railties.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 6.0.3.4
Release: 1%{?dist}
Summary: A toolkit for building modeling frameworks (part of Rails)
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The gem doesn't ship with the test suite.
# You may check it out like so
# git clone https://github.com/rails/rails.git
# cd rails/activemodel && git archive -v -o activemodel-6.0.3.4-tests.txz v6.0.3.4 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may check it out like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.0.3.4-tools.txz v6.0.3.4 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygem(activesupport) = %{version}
%if %{without bootstrap}
BuildRequires: rubygem(railties) = %{version}
%endif
BuildRequires: rubygem(bcrypt) => 3.1.2
BuildRequires: rubygem(builder)
BuildArch: noarch

%description
A toolkit for building modeling frameworks like Active Record. Rich support
for attributes, callbacks, validations, serialization, internationalization,
and testing.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1 -b2

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/tools ..
mv %{_builddir}/test .

%if %{with bootstrap}
# This depends on Rails
mv ./test/cases/railtie_test.rb{,.disable}
%endif

# Run test in order, otherwise we get a lot of errors.
ruby -Ilib:test -e "Dir.glob('./test/**/*_test.rb').sort.each {|t| require t}"
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Oct  8 10:54:54 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to activemodel 6.0.3.4.
  Resolves: rhbz#1877543

* Fri Sep 18 18:07:35 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to activemodel 6.0.3.3.
  Resolves: rhbz#1877543

* Mon Aug 17 04:49:08 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to activemodel 6.0.3.2.
  Resolves: rhbz#1742793

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-2
- Update to ActiveModel 6.0.3.1.
  Resolves: rhbz#1742793

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Active Model 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Active Model 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-2
- Update to Active Model 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Active Model 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Active Model 5.2.0.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-1
- Update to Active Model 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-1
- Update to Active Model 5.1.4.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-1
- Update to Active Model 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-1
- Update to Active Model 5.1.2.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-1
- Update to Active Model 5.1.1.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-1
- Update to Active Model 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-1
- Update to Active Model 5.0.1.

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-1
- Update to Activemodel 5.0.0.1

* Mon Jul 04 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.0-1
- Update to ActiveModel 5.0.0.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 4.2.6-1
- Update to activemodel 4.2.6

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.2-1
- Update to activemodel 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.1-1
- Update to activemodel 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 4.2.5-1
- Update to activemodel 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 4.2.4-1
- Update to activemodel 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 4.2.3-1
- Update to activemodel 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 4.2.2-1
- Update to activemodel 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-2
- Fix: update tests

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-1
- Update to activemodel 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 4.2.0-1
- Update to activemodel 4.2.0

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to activemodel 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to activemodel 4.1.4
- Stabilize test suite

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 4.1.1-1
- Update to ActiveModel 4.1.1

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Fri Apr 11 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-1
- Update to ActiveModel 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 4.0.3-1
- Update to ActiveModel 4.0.3

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.2-1
- Update to ActiveModel 4.0.2
- Fix changelog

* Mon Nov 11 2013 Josef Stribny <jstribny@redhat.com> - 4.0.1-1
- Update to ActiveModel 4.0.1

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to ActiveModel 4.0.0.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.13-1
- Update to ActiveModel 3.2.13.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-1
- Update to ActiveModel 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.11-1
- Update to ActiveModel 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.10-1
- Update to ActiveModel 3.2.10.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-3
- Fixed the Builder dependencies in .gemspec file.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-2
- Relaxed Builder dependnecy.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-1
- Update to ActiveModel 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.7-1
- Update to ActiveModel 3.2.7.

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.6-1
- Update to ActiveModel 3.2.6.
- Remove no longer needed I18n dependency.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.15-1
- Update to ActiveModel 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.13-1
- Update to ActiveModel 3.0.13.

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActiveModel 3.0.11.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.10-1
- Update to ActiveModel 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-1
- Update to ActiveModel 3.0.9

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.5-1
- Update to ActiveModel 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.3-3
- Removed unnecessary clean section.

* Mon Jan 31 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.3-2
- Added build dependencies.

* Tue Jan 25 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.3-1
- Upgraded to activemodel 3.0.3
- Added documentation subpackage
- Added test execution during build
- Removed unnecessary cleanup from install section

* Tue Oct 26 2010 Jozef Zigmund <jzigmund@dhcp-29-238.brq.redhat.com> - 3.0.1-1
- Initial package
