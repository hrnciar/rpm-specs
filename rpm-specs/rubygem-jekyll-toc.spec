%global gem_name jekyll-toc

Name:           rubygem-%{gem_name}
Version:        0.14.0
Release:        1%{?dist}
Summary:        Jekyll Table of Contents plugin
License:        MIT

URL:            https://github.com/toshimaru/jekyll-toc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Patch to disable coverage reporting
Patch0:         00-disable-simplecov.patch

BuildRequires:  git
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.2.2

BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(jekyll) >= 3.5
BuildRequires:  (rubygem(minitest) >= 5.0 with rubygem(minitest) < 6)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(racc)
BuildRequires:  rubygem(rake)

BuildArch:      noarch

%description
A liquid filter plugin for Jekyll which generates a table of contents.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -S git -n %{gem_name}-%{version} -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
rake test
popd


%files
%license %{gem_instdir}/LICENSE.md

%dir %{gem_instdir}

%{gem_instdir}/Appraisals
%{gem_instdir}/gemfiles

%{gem_libdir}

%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.github/


%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/jekyll-toc.gemspec
%{gem_instdir}/test


%changelog
* Sun May 24 2020 Fabio Valentini <decathorpe@gmail.com> - 0.14.0-1
- Update to version 0.14.0.

* Sun Feb 02 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.1-1
- Update to version 0.13.1.

* Fri Jan 31 2020 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-3
- Add BR: rubygem(racc) to fix FTBFS issue.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-1
- Update to version 0.12.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.1-1
- Update to version 0.12.1.

* Sat Apr 06 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.0-1
- Update to version 0.12.0.

* Sun Mar 24 2019 Fabio Valentini <decathorpe@gmail.com> - 0.11.0-1
- Update to version 0.11.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.1-1
- Update to version 0.9.1.

* Wed Oct 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.0-1
- Update to version 0.9.0.

* Sat Oct 20 2018 Fabio Valentini <decathorpe@gmail.com> - 0.8.0-1
- Update to version 0.8.0.

* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.7.1-1
- Initial package

