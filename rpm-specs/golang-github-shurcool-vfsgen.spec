# Generated by go2rpm
%bcond_without check

# https://github.com/shurcooL/vfsgen
%global goipath         github.com/shurcooL/vfsgen
%global commit          92b8a710ab6cab4c09182a1fcf469157bc938f8f

%gometa

%global common_description %{expand:
Package Vfsgen takes an http.FileSystem (likely at go generate time) and
generates Go code that statically implements the provided http.FileSystem.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        0.6%{?dist}
Summary:        Takes an input http.FileSystem and generates code that statically implements it

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/shurcooL/httpfs/vfsutil)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Aug 02 19:12:04 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20200802git92b8a71
- Bump to commit 92b8a710ab6cab4c09182a1fcf469157bc938f8f

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 15:59:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190701git6a9ea43
- Initial package
