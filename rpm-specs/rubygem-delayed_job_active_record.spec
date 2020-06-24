# Generated from delayed_job_active_record-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name delayed_job_active_record

Name: rubygem-%{gem_name}
Version: 4.1.3
Release: 4%{?dist}
Summary: ActiveRecord back-end for DelayedJob
License: MIT
URL: http://github.com/collectiveidea/delayed_job_active_record
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/collectiveidea/delayed_job_active_record.git && cd delayed_job_active_record
# git checkout v4.1.3 && tar czvf delayed_job_active_record-4.1.3-tests.tgz ./spec
Source1: delayed_job_active_record-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(activerecord) >= 3.0
# The test suite needs sample_jobs from delayed_job
# https://github.com/collectiveidea/delayed_job_active_record/issues/18
BuildRequires: rubygem-delayed_job-doc >= 3.0
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
ActiveRecord back-end for Delayed::Job, originally authored by Tobias Luetke.


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
# Move test into the place.
ln -s %{_builddir}/spec spec

# We do not care about test coverage.
sed -i "1,14 s/^/#/" spec/helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/delayed_job_active_record.gemspec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Vít Ondruch <vondruch@redhat.com> - 4.1.3-1
- Update to delayed_job_active_record 4.1.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Vít Ondruch <vondruch@redhat.com> - 4.1.2-1
- Update to delayed_job_active_record 4.1.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Jun Aruga <jaruga@redhat.com> - 4.1.1-1
- Update to 4.1.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Josef Stribny <jstribny@redhat.com> - 4.0.3-1
- Update to 4.0.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 Josef Stribny <jstribny@redhat.com> - 4.0.1-1
- Update to 4.0.1

* Fri Aug 16 2013 Vít Ondruch <vondruch@redhat.com> - 4.0.0-1
- Update to delayed_job_active_record 4.0.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Vít Ondruch <vondruch@redhat.com> - 0.3.3-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.3-1
- Update to delayed_job_active_record 0.3.3.

* Thu May 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.2-1
- Initial package
