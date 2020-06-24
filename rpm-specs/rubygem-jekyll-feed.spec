%global gem_name jekyll-feed

Name:           rubygem-%{gem_name}
Version:        0.13.0
Release:        3%{?dist}
Summary:        Jekyll plugin to generate an Atom feed of your Jekyll posts
License:        MIT

URL:            https://github.com/jekyll/jekyll-feed
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby >= 2.3
BuildRequires:  rubygems-devel
BuildRequires:  ruby(release)

BuildRequires:  rubygem(jekyll)
BuildRequires:  (rubygem(nokogiri) >= 1.6 with rubygem(nokogiri) < 2)
BuildRequires:  rubygem(racc)
BuildRequires:  (rubygem(rspec) >= 3.0 with rubygem(rspec) < 4)
BuildRequires:  rubygem(typhoeus)

BuildArch:      noarch

%description
A Jekyll plugin to generate an Atom feed of your Jekyll posts.


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


%check
pushd .%{gem_instdir}

# Tests fail when LANG is not set to a UTF-8 locale
LANG=C.UTF-8 rspec spec

popd


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}
%{gem_instdir}/script

%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}

%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/appveyor.yml
%exclude %{gem_instdir}/jekyll-feed.gemspec

%files doc
%doc %{gem_instdir}/History.markdown
%doc %{gem_instdir}/README.md

%doc %{gem_docdir}

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%exclude %{gem_instdir}/.rspec


%changelog
* Fri Jan 31 2020 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-3
- Add BR: rubygem(racc) to fix FTBFS issue.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-1
- Update to version 0.13.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 31 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.1-1
- Update to version 0.12.1.

* Fri Mar 22 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.0-1
- Update to version 0.12.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.0-2
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Sep 10 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.0-1
- Update to version 0.11.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.10.0-1
- Update to version 0.10.0.
- Re-enable tests.

* Mon Jun 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.3-2
- Temporarily disable tests.

* Mon Apr 23 2018 Fabio Valentini <decathorpe@gmail.com> - 0.9.3-1
- Initial package

