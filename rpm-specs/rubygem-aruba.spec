# Generated from aruba-0.4.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name aruba

Summary: CLI Steps for Cucumber, hand-crafted for you in Aruba
Name: rubygem-%{gem_name}
Version: 0.14.14
Release: 2%{?dist}
# aruba itself is MIT
# icons in templates/images are CC-BY
# jquery.js itself is MIT or GPLv2
# jquery.js includes sizzle.js, which is MIT or BSD or GPLv2
License: MIT and CC-BY and (MIT or GPLv2) and (MIT or BSD or GPLv2)
URL: http://github.com/cucumber/aruba
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(cucumber) >= 1.3.19
BuildRequires: rubygem(childprocess) >= 0.5.6
BuildRequires: rubygem(ffi) >= 1.9.10
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(pry)
BuildRequires: rubygem(rspec) >= 3
BuildRequires: rubygem(contracts) >= 0.9
BuildRequires: rubygem(thor) >= 0.19
# features/steps/command/shell.feature:97 # Scenario: Running python commands
BuildRequires: /usr/bin/python3
BuildArch: noarch

%description
Aruba is Cucumber extension for Command line applications written
in any programming language.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%gemspec_remove_dep -g childprocess '>= 0.6.3'

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.[^.]* \
	Gemfile \
	Rakefile \
	appveyor.yml \
	%{gem_name}.gemspec \
	cucumber.yml \
	config/ \
	fixtures/ \
	spec/ \
	script/ \
	%{nil}

%check
pushd .%{gem_instdir}
# Drop the fuubar dependency.
rm .rspec

# We don't care about code coverage.
# We don't need Bundler.
sed -i spec/spec_helper.rb \
	-e '\@[sS]imple[Cc]ov@d' \
	-e '\@[Bb]undler@d' \
	%{nil}

RUBYOPT=-rtime rspec spec

# We don't care about code coverage.
sed -i features/support/env.rb \
	-e '\@require.*simplecov@d'
> features/support/simplecov_setup.rb

# Let the test cli-app find Aruba.
sed -i fixtures/cli-app/spec/spec_helper.rb \
	-e "\@\$LOAD_PATH@s|\.\./\.\./lib|$(pwd)/lib|"

# /usr/bin/python is reporting deprecation warning :/
# No need to modify @requires-python (in run_commands.feature and hooks.rb)
if ! grep -q python3 features/steps/command/shell.feature
then
	sed -i features/03_testing_frameworks/cucumber/steps/command/run_commands_which_require_a_shell.feature \
		-e 's|python|python3|'
	sed -i lib/aruba/generators/script_file.rb  \
		-e '\@interpreter@s|A-Z|A-Z0-9|'
	sed -i features/01_getting_started_with_aruba/run_commands.feature \
		-e '\@[^-]python@s|python|python3|'
fi

# Get rid of Bundler
sed -i Rakefile \
	-e '\@[Bb]undler@d' \
	-e 's|bundle exec ||' \
	%{nil}

# Adjust test cases referring to $HOME.
sed -i features/04_aruba_api/core/expand_path.feature -e "s|/home/\[\^/\]+|$(echo $HOME)|" 
sed -i features/02_configure_aruba/home_directory.feature \
	-e "\@Scenario: Default value@,\@Scenario@s|/home/|$(echo $HOME)|"
sed -i features/02_configure_aruba/home_directory.feature \
	-e "\@Set to aruba's working directory@,\@Scenario@s|/home/|$(echo $HOME)/|"

# Make the Aruba always awailable.
RUBYOPT=-I$(pwd)/lib cucumber
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_instdir}/bin/
%exclude %{gem_instdir}/config
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/TODO.md
%{gem_instdir}/doc/
%{gem_instdir}/features/
%{gem_instdir}/templates/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.14-1
- 0.14.14

* Thu Dec 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.13-1
- 0.14.13

* Tue Nov  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.12-1
- 0.14.12

* Sat Aug 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.11-1
- 0.14.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.9-1
- 0.14.9

* Wed Feb 27 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.8-1
- 0.14.8

* Tue Feb 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.7-3
- Some cleanup

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Vít Ondruch <vondruch@redhat.com>
- Enable test suite.

* Tue Jan 29 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.7-1
- 0.14.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.6-1
- 0.14.6

* Fri Apr  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.5-1
- 0.14.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.3-1
- 0.14.3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  2 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.2-1
- 0.14.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.2-1
- 0.6.2

* Mon Sep  1 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.1-1
- 0.6.1

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0-1
- 0.6.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.4-1
- 0.5.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Josef Stribny <jstribny@redhat.com> - 0.5.2-1
- Update to aruba 0.5.2

* Sat Feb 23 2013 Vít Ondruch <vondruch@redhat.com> - 0.4.11-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.11-5
- Disable tests that do not actually test anything (patch from upstream).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.11-2
- Remove the ffi dependency and add conflicts with the problematic version.

* Fri Feb 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.11-1
- Initial package
