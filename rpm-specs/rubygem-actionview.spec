%global gem_name actionview

# Circular dependency with rubygem-railties.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 6.0.3.4
Release: 1%{?dist}
Summary: Rendering framework putting the V in MVC (part of Rails)
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/actionview && git archive -v -o actionview-6.0.3.4-tests.txz v6.0.3.4 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may get them like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.0.3.4-tools.txz v6.0.3.4 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{without bootstrap}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(sqlite3)
%endif
BuildArch: noarch

%description
Simple, battle-tested conventions and helpers for building web pages.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
# This requires activerecord in rails git structure
ln -s %{gem_dir}/gems/activerecord-%{version}%{?prerelease}/ .%{gem_dir}/gems/activerecord

pushd .%{gem_instdir}
ln -s %{_builddir}/tools ..
mv %{_builddir}/test .

mv test/activerecord/controller_runtime_test.rb{,.disable}

# Run separately as we need to avoid superclass mismatch errors
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; ruby -Itest -- '{}' || exit 255"

popd
%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG.md

%changelog
* Thu Oct  8 11:38:41 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to actionview 6.0.3.4.
  Resolves: rhbz#1877500

* Tue Sep 22 00:37:39 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to actionview 6.0.3.3.
  Resolves: rhbz#1877500

* Mon Aug 17 04:56:29 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to actionview 6.0.3.2.
  Resolves: rhbz#1742791

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to ActionView 6.0.3.1.
  Resolves: rhbz#1742791

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Action View 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Action View 5.2.2.1.

* Thu Feb 07 2019 Vít Ondruch <vondruch@redhat.com> - 5.2.2-4
- Drop unnecessary erubis dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-2
- Update to Action View 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Action View 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-2
- Enable tests.

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Action View 5.2.0.

* Mon Feb 19 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-2
- Enable tests.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-1
- Update to Action View 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-2
- Enable tests.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-1
- Update to Action View 5.1.4.

* Sat Aug 12 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-2
- Enable tests.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-1
- Update to Action View 5.1.3.

* Tue Aug 01 2017 Vít Ondruch <vondruch@redhat.com> - 5.1.2-4
- Prevent negative IDs in output of #inspect to fix test failures.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-2
- Enable tests.

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-1
- Update to Action View 5.1.2.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-1
- Update to Action View 5.1.1.

* Tue Mar 07 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-2
- Enable tests.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-1
- Update to Action View 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-2
- Enable tests.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-1
- Update to Action View 5.0.1.

* Tue Aug 16 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-2
- Enable tests

* Tue Aug 16 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-2
- Enable tests

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-1
- Update to Actionview 5.0.0.1

* Fri Jul 08 2016 Jun Aruga <jaruga@redhat.com> - 5.0.0-1
- Update to actionview 5.0.0

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 4.2.6-2
- Enable tests

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 4.2.6-1
- Update to actionview 4.2.6

* Thu Mar 03 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.2-2
- Enable tests

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.2-1
- Update to actionview 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.1-2
- Enable tests

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.1-1
- Update to actionview 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 4.2.5-2
- Enable tests

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 4.2.5-1
- Update to actionview 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 4.2.4-2
- Enable tests

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 4.2.4-1
- Update to actionview 4.2.4

* Wed Jul 01 2015 Josef Stribny <jstribny@redhat.com> - 4.2.3-2
- Enable tests

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 4.2.3-1
- Update to actionview 4.2.3

* Tue Jun 23 2015 Josef Stribny <jstribny@redhat.com> - 4.2.2-2
- Run tests

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 4.2.2-1
- Update to actionview 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-2
- Run tests

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-1
- Update to actionview 4.2.1

* Fri Feb 13 2015 Josef Stribny <jstribny@redhat.com> - 4.2.0-2
- Run tests

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 4.2.0-1
- Update to actionview 4.2.0

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to actionview 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to actionview 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 4.1.1-1
- Update to ActionView 4.1.1

* Tue Apr 15 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-2
- Unpack test suite in %%check
- Adjust tests to run with all dependencies

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-1
- Initial package
