%global gem_name jekyll-seo-tag

Name:           rubygem-%{gem_name}
Version:        2.6.1
Release:        3%{?dist}
Summary:        Jekyll plugin to add SEO metadata tags
License:        MIT

URL:            https://github.com/benbalter/jekyll-seo-tag
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.3.0

BuildArch:      noarch

%description
A Jekyll plugin to add metadata tags for search engines and social networks to
better index and display your site's content.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}

%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/jekyll-seo-tag.gemspec

%{gem_libdir}

%{gem_instdir}/script

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.markdown
%doc %{gem_instdir}/docs

%exclude %{gem_instdir}/.rspec

%{gem_instdir}/Gemfile


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.1-1
- Update to version 2.6.1.

* Sat Mar 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.6.0-1
- Update to version 2.6.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 2.5.0-1
- Initial package

