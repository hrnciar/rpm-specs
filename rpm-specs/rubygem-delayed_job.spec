# Generated from delayed_job-2.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name delayed_job

Name: rubygem-%{gem_name}
Version: 4.1.5
Release: 4%{?dist}
Summary: Database-backed asynchronous priority queue system
License: MIT
URL: http://github.com/collectiveidea/delayed_job
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(actionmailer) => 3.0.0
BuildRequires: rubygem(activerecord) => 3.0.0
BuildRequires: rubygem(sqlite3) => 1.3.0
BuildArch: noarch

%description
Delayed_job (or DJ) encapsulates the common pattern of asynchronously
executing longer tasks in the background. It is a direct extraction from
Shopify where the job table is responsible for a multitude of core tasks.


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
pushd .%{gem_instdir}
# SimpleCov and Coverall are not necessary
sed -i "1,11 s/^/#/" spec/helper.rb
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%{gem_instdir}/recipes
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/contrib
%{gem_instdir}/Rakefile
%{gem_instdir}/delayed_job.gemspec
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Vít Ondruch <vondruch@redhat.com> - 4.1.5-1
- Update to Delayed Job 4.1.5.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Vít Ondruch <vondruch@redhat.com> - 4.1.4-1
- Update to delayed_job 4.1.4.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Vít Ondruch <vondruch@redhat.com> - 4.1.3-1
- Update to delayed_job 4.1.3.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Vít Ondruch <vondruch@redhat.com> - 4.1.2-1
- Update to delayed_job 4.1.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Josef Stribny <jstribny@redhat.com> - 4.0.6-1
- Update to 4.0.6

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Josef Stribny <jstribny@redhat.com> - 4.0.1-1
- Update to delayed_job 4.0.1

* Mon Aug 12 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to delayed_job 4.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 3.0.2-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.2-1
- Update to delayed_job 3.0.2.

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 2.1.4-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.4-1
- Update to the delayed_job 2.1.4.

* Thu Feb 10 2011 Vít Ondruch <vondruch@redhat.com> - 2.1.3-1
- Initial package
