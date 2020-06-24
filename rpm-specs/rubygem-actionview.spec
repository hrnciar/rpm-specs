%global gem_name actionview

%{?_with_bootstrap: %global bootstrap 1}

Name: rubygem-%{gem_name}
Version: 5.2.3
Release: 4%{?dist}
Summary: Rendering framework putting the V in MVC (part of Rails)
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/rails/rails.git && cd rails/actionview/
# git checkout v5.2.3 && tar czvf actionview-5.2.3-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
# Fix ResolverCacheTest#test_inspect_shields_cache_internals test failures
# due to negative object ID.
# https://github.com/rails/rails/pull/28902
Patch0: rubygem-actionview-5.1.2-Prevent-negative-IDs-in-output-of-inspect.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if ! 0%{?bootstrap}
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
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p2
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if ! 0%{?bootstrap}
%check
# This requires activerecord in rails git structure
ln -s %{gem_dir}/gems/activerecord-%{version}/ .%{gem_dir}/gems/activerecord

pushd .%{gem_instdir}

tar xzvf %{SOURCE1} -C .

# Run separately as we need to avoid superclass mismatch errors
for t in {actionpack,activerecord,template}; do
  ruby -Ilib:test -e "Dir.glob('./test/$t/**/*_test.rb').each {|t| require t}"
done

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
