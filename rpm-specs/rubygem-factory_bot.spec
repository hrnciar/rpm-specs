%global gem_name factory_bot

Name: rubygem-%{gem_name}
Version: 4.10.0
Release: 4%{?dist}
Summary: Framework and DSL for defining and using model instance factories
License: MIT
URL: https://github.com/thoughtbot/factory_bot
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/thoughtbot/factory_bot.git && cd factory_bot
# git checkout v4.10.0 && tar czvf factory_bot-4.10.0-specs.tar.gz spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
# git clone https://github.com/thoughtbot/factory_bot.git && cd factory_bot
# git checkout v4.10.0 && tar czvf factory_bot-4.10.0-features.tar.gz features/
Source2: %{gem_name}-%{version}-features.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-its)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(timecop)
BuildRequires: %{_bindir}/cucumber
BuildRequires: rubygem(aruba)
BuildArch: noarch
# Gem was renamed.
# https://github.com/thoughtbot/factory_bot/commit/e083f4a904ae30d170872385d4be3b37d44276e5
Obsoletes: rubygem-factory_girl < 4.10.0

%description
Framework and DSL for defining and using factories - less error-prone,
more explicit, and all-around easier to work with than fixtures.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
# Unpack Source1 and Source2
%setup -q -n %{gem_name}-%{version} -b 1 -b 2

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Symlinks don't work for this test suite
cp -a %{_builddir}/spec .

# We don't care about coverage.
sed -i "/simplecov/ s/^/#/" spec/spec_helper.rb

rspec -rfileutils spec

ln -s %{_builddir}/features .
sed -i "/simplecov/ s/^/#/" features/support/env.rb

cucumber
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/factory_bot.gemspec
# Delete factory_girl.gemspec
# https://github.com/thoughtbot/factory_bot/pull/1161
%exclude %{gem_instdir}/factory_girl.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/Gemfile.lock

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Appraisals
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/GETTING_STARTED.md
%doc %{gem_instdir}/NAME.md
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/gemfiles
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber.yml

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Pavel Valena <pvalena@redhat.com> - 4.10.0-1
- Upgrade to factory_bot 4.10.0.
- Renamed from factory_girl to factory_bot.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Vít Ondruch <vondruch@redhat.com> - 4.8.0-1
- Update to factory_girl 4.8.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Vít Ondruch <vondruch@redhat.com> - 2.3.2-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.3.2-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 13 2011 Michal Fojtik <mfojtik@redhat.com> - 2.3.2-1
- Version bump

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 1.3.2-5
- Fixes to build in rawhide

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-3
- Replaced path with path macro

* Wed Oct 13 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-2
- Rakefile fixing moved to a separate patch
- Fixed unneeded Requires
- Fixed directory ownership on doc subpackage
- README and LICENSE moved back to main package

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.2-1
- Initial package
