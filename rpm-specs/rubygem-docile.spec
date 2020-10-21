%global gem_name docile

Summary:       Docile keeps your Ruby DSLs tame and well-behaved
Name:          rubygem-%{gem_name}
Version:       1.1.5
Release:       11%{?dist}
License:       MIT
URL:           https://ms-ati.github.com/docile/
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Requires:      ruby(release)
Requires:      ruby(rubygems)
%endif
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
# coveralls is now optional for tests
# Add back when coveralls is in Fedora
#BuildRequires: rubygem(coveralls)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(redcarpet)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(yard)
BuildArch:     noarch
%if 0%{?fc19} || 0%{?fc20} || 0%{?el7}
Provides:      rubygem(%{gem_name}) = %{version}
%endif

%description
Docile turns any Ruby object into a DSL.
Especially useful with the Builder pattern.


%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.coveralls.yml,.gitignore,.rspec,.ruby-gemset,.ruby-version,.travis.yml,.yard*}

%check
rspec -Ilib spec

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/docile.gemspec
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/on_what.rb
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Troy Dawson <tdawson@redhat.com> - 1.1.5-1
- Updated to latest release

* Fri Jun 13 2014 Troy Dawson <tdawson@redhat.com> - 1.1.4-1
- Update to version 1.1.4
- Tests now run without coveralls

* Wed Apr 02 2014 Troy Dawson <tdawson@redhat.com> - 1.1.3-1
- Initial package
