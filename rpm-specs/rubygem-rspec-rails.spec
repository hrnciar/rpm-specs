# Generated from rspec-rails-2.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rspec-rails

# Circular dependency with rubygem-ammeter.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 3.9.0
Release: 2%{?dist}
Summary: RSpec for Rails
License: MIT
URL: https://github.com/rspec/rspec-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rspec/rspec-rails.git && cd rspec-rails
# git archive -v -o rspec-rails-3.9.0-tests.tar.gz v3.9.0 features/ spec/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
#BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(actionmailer)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(ammeter)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sqlite3)
%endif
BuildArch: noarch

%description
rspec-rails is a testing framework for Rails 3+.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%if %{without bootstrap}
%check
pushd .%{gem_instdir}
cp -a %{_builddir}/features features
cp -a %{_builddir}/spec spec

# Bundler is used to execute two tests, so give him Gemfile.
echo "gem 'rspec', :require => false" > Gemfile

# I have no idea why this is passing upstream, since when RSpec are not supposed
# to be loaded, then RSpec::Support can't exist.
sed -i '/uninitialized constant RSpec::Support/ s/::Support//' spec/sanity_check_spec.rb

# Avoid git dependency. This is not funcitonal test anyway, just style check.
sed -i 's/`git ls-files -z`/""/' spec/rspec/rails_spec.rb

rspec -rspec_helper -rbundler spec

# Needs to generate a rails test application or ship pregenerated one (see
# generate:app rake task). This would be quite fragile.
# cucumber
popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Capybara.md
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.md


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.0-1
- 3.9.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Vít Ondruch <vondruch@redhat.com> - 3.8.2-1
- Update to rspec-rails 3.8.2.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.8.1-1
- 3.8.1
- Once disable tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.1-1
- Enable test suite again

* Mon Nov 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.1-0.1
- 3.7.1
- Once disable tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.0-2
- Enable test suite again

* Sun May  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.0-1
- 3.6.0
- Once disable tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Vít Ondruch <vondruch@redhat.com> - 3.5.2-1
- Update to rspec-rails 3.5.2.

* Mon Jul 25 2016 Vít Ondruch <vondruch@redhat.com> - 3.5.1-2
- Re-enable test suite.

* Sun Jul 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.og> - 3.5.1-1
- Update to rspec-rails 3.5.1.
- Once disable tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Vít Ondruch <vondruch@redhat.com> - 3.4.0-2
- Re-enable tests.

* Tue Dec 08 2015 Mamoru TASAKA <mtasaka@fedoraproject.og> - 3.4.0-1
- Update to rspec-rails 3.4.0.
- Once disable tests

* Tue Aug 04 2015 Vít Ondruch <vondruch@redhat.com> - 3.3.3-1
- Update to rspec-rails 3.3.3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Vít Ondruch <vondruch@redhat.com> - 3.2.1-1
- Update to rspec-rails 3.2.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Vít Ondruch <vondruch@redhat.com> - 2.14.1-1
- Update to rspec-rails 2.14.1.

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.og> - 2.14.0-2
- Enable test suite again

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.og> - 2.14.0-1
- Update to rspec-rails 2.14.0
- Still tests is disabled for now

* Mon Aug 12 2013 Josef Stribny <jstribny@redhat.com> - 2.13.0-4
- Relax Rails deps and disable tests for now

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-2
- Enable test suite again

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-1
- Update to rspec-rails 2.13.0

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 2.12.0-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.0-2
- Enable test suite again

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.0-1
- Update to rspec-rails 2.12.0

* Tue Oct 16 2012 Vít Ondruch <vondruch@redhat.com> - 2.11.4-1
- Update to rspec-rails 2.11.4.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 2.11.0-1
- Update to rspec-rails 2.11.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 2.8.1-2
- Tests enabled.

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 2.8.1-1
- Rebuilt for Ruby 1.9.3.
- Update to rspec-rails 2.8.1.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.1-3
- Fixed .gemspec to contain correct dependencies (rhbz#747405).

* Tue Aug 23 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.1-2
- Rebuilt due to the trailing slash bug of rpm-4.9.1

* Tue Jun 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.1-1
- Updated to the rspec-rails 2.6.1

* Mon May 23 2011 Vít Ondruch <vondruch@redhat.com> - 2.6.0-1
- Initial package
