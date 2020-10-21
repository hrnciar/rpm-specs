# Generated by go2rpm
%bcond_without check

# https://github.com/emirpasic/gods
%global goipath         github.com/emirpasic/gods
Version:                1.12.0

%gometa

%global common_description %{expand:
GoDS (Go Data Structures)

Implementation of various data structures and algorithms in Go.

Containers (Sets, Lists, Stacks, Maps, Trees), Sets (HashSet, TreeSet), Lists
(ArrayList, SinglyLinkedList, DoublyLinkedList), Stacks (LinkedListStack,
ArrayStack), Maps (HashMap, TreeMap, HashBidiMap, TreeBidiMap), Trees
(RedBlackTree, AVLTree, BTree, BinaryHeap), Comparators, Iterators, Enumerables,
Sort, JSON}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Implementation of various data structures and algorithms in Go

License:        BSD and ISC
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 22:15:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.12.0-1
- Release 1.12.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.9.0-3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 Dominik Mierzejewski <dominik@greysector.net> - 1.9.0-1
- First package for Fedora
