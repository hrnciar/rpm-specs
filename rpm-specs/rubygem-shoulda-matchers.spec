# Generated from shoulda-matchers-2.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name shoulda-matchers

Name: rubygem-%{gem_name}
Version: 4.1.2
Release: 5%{?dist}
Summary: Simple one-liner tests for common Rails functionality
License: MIT
URL: https://matchers.shoulda.io/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/thoughtbot/shoulda-matchers.git && cd shoulda-matchers
# git archive -v -o shoulda-matchers-4.1.2-specs.tar.gz v4.1.2 spec/
Source1: shoulda-matchers-4.1.2-specs.tar.gz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bcrypt)
BuildRequires: rubygem(jbuilder)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(rails-controller-testing)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-rails)
BuildRequires: rubygem(shoulda-context)
BuildRequires: rubygem(spring)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer,
more complex, and error-prone.


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



%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

# It is easier to recreate the Gemfile to use local versions of gems.
cat << GF > Gemfile
source 'https://rubygems.org'

gem 'bcrypt'
gem 'rails'
gem 'rails-controller-testing'
gem 'rspec'
gem 'rspec-rails'
gem 'sqlite3'
gem 'spring'
GF

# Pry is useless for our purposes.
sed -i "/require 'pry/ s/^/#/" spec/spec_helper.rb

# Avoid Appraisal and Bundler.
sed -i "/current_bundle/ s/^/#/" spec/acceptance_spec_helper.rb
sed -i "/assert_appraisal/ s/^/#/" spec/acceptance_spec_helper.rb
sed -i "/current_bundle/ s/^/#/" spec/support/unit/load_environment.rb
sed -i "/assert_appraisal/ s/^/#/" spec/support/unit/load_environment.rb

# Avoid bootsnap, listen, puma and sprockets dependencies.
sed -i "/def rails_new_command/,/^    end$/ {
  /\]/i\          '--skip-listen',
}" spec/support/unit/rails_application.rb
sed -i '/rails new/ s/"$/ --skip-bootsnap --skip-listen --skip-puma --skip-sprockets"/' spec/support/acceptance/helpers/step_helpers.rb

bundle exec rspec spec/unit

# Don't test against PostgreSQL, it would just complicate everything.
sed -i "/bundle.add_gem 'pg'/ s/^/#/" spec/support/acceptance/helpers/step_helpers.rb
# spring-commands-rspec is not in Fedora yet, but the test suite looks to pass
# without it just fine.
sed -i "/add_gem 'spring-commands-rspec'/ s/^/#/" spec/support/acceptance/helpers/step_helpers.rb
# Remove useless test dependencies.
sed -i "/updating_bundle do |bundle|/a \\
        bundle.remove_gem 'capybara'" spec/support/acceptance/helpers/step_helpers.rb
sed -i "/updating_bundle do |bundle|/a \\
        bundle.remove_gem 'selenium-webdriver'" spec/support/acceptance/helpers/step_helpers.rb
sed -i "/updating_bundle do |bundle|/a \\
        bundle.remove_gem 'chromedriver-helper'" spec/support/acceptance/helpers/step_helpers.rb

# Remove minitest-reporters dependency
# https://github.com/thoughtbot/shoulda-matchers/pull/1251
sed -i "/def add_minitest_to_project/,/^    end$/ {
  /initest.*eporters/ s/^/#/
}" spec/support/acceptance/helpers/step_helpers.rb
sed -i '/run_n_unit_tests/ s/courier_test\.rb/courier_test.rb - -v/' spec/acceptance/independent_matchers_spec.rb

# Keep the unrestricted SQLite3 dependency.
sed -i "/sqlite3/ s/^/#/" spec/support/acceptance/helpers/step_helpers.rb

bundle exec rspec spec/acceptance

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/shoulda-matchers.gemspec

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Vít Ondruch <vondruch@redhat.com> - 4.1.2-2
- Remove unnecessary BR: rubygem(minitest-reporters).

* Thu Nov 07 2019 Vít Ondruch <vondruch@redhat.com> - 4.1.2-1
- Update to should-matchers 4.1.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Vít Ondruch <vondruch@redhat.com> - 3.1.2-1
- Update to should-matchers 3.1.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 26 2015 Vít Ondruch <vondruch@redhat.com> - 2.8.0-1
- Update to should-matchers 2.8.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 07 2014 Vít Ondruch <vondruch@redhat.com> - 2.6.1-3
- Workaround RoR 4.1.2+ compatibility issue.
- Relax Rake dependency.

* Thu Jul 03 2014 Vít Ondruch <vondruch@redhat.com> - 2.6.1-2
- Add missing BR: rubygem(shoulda-context).
- Updated upstream URL.
- Relaxed BR: ruby dependency.

* Mon Jun 30 2014 Vít Ondruch <vondruch@redhat.com> - 2.6.1-1
- Initial package
