%global gem_name cucumber-rails


%global enable_cucumber_tests 1

Name: rubygem-%{gem_name}
Version: 1.8.0
Release: 3%{?dist}
Summary: Cucumber Generators and Runtime for Rails
License: MIT
URL: http://cukes.info
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(ammeter)
BuildRequires: rubygem(sqlite3)

%if 0%{enable_cucumber_tests}
# The integration test dependencies:
BuildRequires: %{_bindir}/cucumber
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(aruba)
BuildRequires: rubygem(database_cleaner)
BuildRequires: rubygem(factory_bot)

# Test app dependencies.
BuildRequires: %{_bindir}/node
BuildRequires: rubygem(byebug)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(coffee-rails)
BuildRequires: rubygem(jbuilder)
BuildRequires: rubygem(sass-rails)
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(turbolinks)
BuildRequires: rubygem(uglifier)
BuildRequires: rubygem(web-console)
BuildRequires: rubygem(rails)
%endif
BuildArch: noarch

%description
Cucumber Generator and Runtime for Rails.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

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
cp ../%{gem_name}-%{version}.gemspec .%{gem_instdir}/%{gem_name}.gemspec

pushd .%{gem_instdir}

%if 0%{enable_cucumber_tests}
%gemspec_remove_dep -s %{gem_name}.gemspec -g ammeter -d ">= 1.1.4"
%gemspec_remove_dep -s %{gem_name}.gemspec -g appraisal -d "~> 2.2"
%gemspec_remove_dep -s %{gem_name}.gemspec -g yard -d "~> 0.9.10"
%gemspec_remove_dep -s %{gem_name}.gemspec -g rdoc -d ">= 6.0"
%gemspec_remove_dep -s %{gem_name}.gemspec -g rubocop -d "~> 0.72.0"
%gemspec_remove_dep -s %{gem_name}.gemspec -g rubocop-performance -d "~> 1.4.0"
%gemspec_remove_dep -s %{gem_name}.gemspec -g rubocop-rspec -d "~> 1.33.0"
%gemspec_remove_dep -s %{gem_name}.gemspec -g rake -d ">= 12.0"
%gemspec_remove_dep -s %{gem_name}.gemspec -g rspec -d "~> 3.6"
%gemspec_add_dep -s %{gem_name}.gemspec -g rspec-expectations -d "~> 3.6"

%gemspec_remove_dep -s %{gem_name}.gemspec -g capybara ">= 2.12", "< 4"
%gemspec_remove_dep -s %{gem_name}.gemspec -g mime-types ">= 2.0", "< 4"
%gemspec_remove_dep -s %{gem_name}.gemspec -g nokogiri "~> 1.8"
%gemspec_remove_dep -s %{gem_name}.gemspec -g railties ">= 4.2", "< 7"
%endif

rspec spec

%if 0%{enable_cucumber_tests}
# Do not download anything, use locally installed packages.
sed -i "s/'bundle install'/'bundle install --local'/" features/support/cucumber_rails_helper.rb

# We have more recent SQLite in Feodra.
sed -i "/sqlite3/ s/~> 1\.3\.13/>= 1\.3\.13/" features/support/cucumber_rails_helper.rb

# There is just old selenium-webdriver available in Fedora.
sed -i "/selenium-webdriver/ s/~> 3\.11/>= 2/" features/support/cucumber_rails_helper.rb

# We don't have chromedriver-helper in Fedora.
sed -i "/run_command_and_stop 'bundle install --local'/i\\
    overwrite_file('Gemfile', File.read(expand_path('Gemfile')).gsub!(/gem 'chromedriver-helper'/, '#\\\0'))" features/support/cucumber_rails_helper.rb

# Get Puma out of the game. The dependency in Gemfile is too tight and default
# Ruby WEBrick must be just fine.
sed -i "/run_command_and_stop 'bundle install --local'/i\\
    overwrite_file('Gemfile', File.read(expand_path('Gemfile')).gsub!(/gem 'puma'/, '#\\\0'))" features/support/cucumber_rails_helper.rb

# The test requires Firefox, which requires Xvfb, etc.
sed -i '/^  Scenario: Use a particular driver$/i\  @firefox' features/capybara_javascript_drivers.feature
sed -i '/^  Scenario: Mixed DB access$/i\  @firefox' features/capybara_javascript_drivers.feature
sed -i '/^  Scenario: See a widget$/i\  @firefox' features/emulate_javascript.feature

cucumber --tags 'not @firefox'
%endif
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/config/.gitignore
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/bin
%{gem_instdir}/config
%exclude %{gem_instdir}/config/.gitignore
%{gem_instdir}/cucumber-rails.gemspec
%{gem_instdir}/dev_tasks
%{gem_instdir}/features
%{gem_instdir}/gemfiles
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Vít Ondruch <vondruch@redhat.com> - 1.8.0-2
- Use WEBrick instead of Puma for testing.

* Wed Aug 21 2019 Vít Ondruch <vondruch@redhat.com> - 1.8.0-1
- Update to cucumber-rails 1.8.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Vít Ondruch <vondruch@redhat.com> - 1.5.0-5
- Replace factory_girl by factory_bot to fix FTBFS (rhbz#1675913).

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Vít Ondruch <vondruch@redhat.com> - 1.5.0-4
- Fix FTFSB caused by updated RoR and Capybara (rhzb#1606180).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Vít Ondruch <vondruch@redhat.com> - 1.5.0-1
- Update to cucumber-rails 1.5.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 10 2016 Vít Ondruch <vondruch@redhat.com> - 1.4.4-1
- Update to cucumber-rails 1.4.4.

* Thu Apr 14 2016 Vít Ondruch <vondruch@redhat.com> - 1.4.3-1
- Update to cucumber-rails 1.4.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Vít Ondruch <vondruch@redhat.com> - 1.4.2-1
- Update to cucumber-rails 1.4.2.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 16 2014 Josef Stribny <jstribny@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Josef Stribny <jstribny@redhat.com> - 1.3.0-5
- Fix: require rubygem-nokogiri and rubygem-capybara for runtime

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.0-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.0-1
- Update to cucumber-rails 1.3.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.2-9
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.2-1
- Update to latest upstream release

* Fri Jul 08 2011 Chris Lalancette <clalance@redhat.com> - 0.3.2-7
- Remove the check section as it doesn't work currently
- Re-arrange the spec to install the gem during prep

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Michal Fojtik <mfojtik@redhat.com> - 0.3.2-5
- Fixed wrong email in changelog
- Fixed version in cucumber dependency
- Fixed attributes on doc subpackage

* Mon Oct 11 2010 Michal Fojtik <mfojtik@redhat.com> - 0.3.2-4
- Moved tests and documentation to doc subpackage
- Fixed licence tag
- Removed unused macros
- Fixed version dependencies

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 0.3.2-3
- Added nokogiri gem to dependencies

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 0.3.2-2
- Added missing cucumber dependency for build

* Fri Oct 01 2010 Michal Fojtik <mfojtik@redhat.com> - 0.3.2-1
- Initial package
