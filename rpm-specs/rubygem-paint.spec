%global gem_name paint

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 7%{?dist}
Summary: Terminal painter
License: MIT
URL: https://github.com/janlelis/paint
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch
#tests
BuildRequires: rubygem(rspec-core)

%description
Paint manages terminal colors and effects for you. It combines the strengths
of term-ansicolor, rainbow and other similar projects into a simple to use,
however still flexible terminal colorization gem with no core extensions by
default.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm %{buildroot}%{gem_instdir}/{.travis.yml,.rspec}

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/data
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.gemtest
%license %{gem_instdir}/MIT-LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Dominic Cleal <dominic@cleal.org> - 2.0.0-1
- rebase to paint-2.0.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Miroslav Suchý <msuchy@redhat.com> 1.0.0-1
- rebase to paint-1.0.0

* Tue Nov 25 2014 Miroslav Suchý <miroslav@suchy.cz> 0.9.0-2
- rebase to 0.9.0

* Tue Jan 21 2014 Miroslav Suchý <miroslav@suchy.cz> 0.8.7-1
- rebase paint-0.8.7.gem

* Mon Aug 26 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-3
- 998459 - move README and LICENSE to main package
- 998459 - remove excessive cp
- 998459 - use virtual requires
- 998459 - remove ruby mri requires

* Mon Aug 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-2
- enable tests
- fix files section

* Mon Aug 19 2013 Miroslav Suchý <msuchy@redhat.com> 0.8.6-1
- initial package

